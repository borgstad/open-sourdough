import cv2
import datetime
from pathlib import Path
import paramiko
from open_sourdough_monitor import settings, models


class SourDoughMonitor:
    def __init__(
        self,
    ):
        self.fs = self.connect_fs()
        self.db = self.connect_db()

    def take_picture(self):
        camera = cv2.VideoCapture(0)
        _, image = camera.read()
        now = datetime.datetime.utcnow()
        filename = now.strftime("%Y-%m-%d_%H-%M-%S-%f") + ".jpg"
        abs_filepath = str(settings.OPEN_SOURDOUGH_REMOTE_IMAGE_DIR / filename)
        cv2.imwrite(filename, image)
        with self.fs.open_sftp() as sftp:
            with models.session_factory() as session:
                sftp.put(filename, abs_filepath)
                session.add(models.SourDoughImages(abs_filepath, now))
                session.commit()
                session.close()
                Path(filename).unlink()

    def connect_fs(self):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(
            hostname=settings.OPEN_SOURDOUGH_SSH_HOSTNAME,
            port=settings.OPEN_SOURDOUGH_SSH_PORT,
            username=settings.OPEN_SOURDOUGH_SSH_USERNAME,
        )
        return client

    def connect_db(self):
        return


if __name__ == "__main__":
    SourDoughMonitor().take_picture()
