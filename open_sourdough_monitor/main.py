import datetime
import time

import cv2

from open_sourdough_monitor import models, settings


class SourDoughMonitor:
    def __init__(
        self,
        session_time: datetime.timedelta,
        picture_interval: datetime.timedelta = datetime.timedelta(minutes=1),
    ):
        self.session_id = models.get_latest_id() + 1
        self.session_end_time = datetime.datetime.now() + session_time
        self.picture_interval = picture_interval

    def start_session(self):
        while datetime.datetime.now() < self.session_end_time:
            self.take_picture()
            time.sleep(self.picture_interval.seconds)

    def take_picture(self):
        camera = cv2.VideoCapture(0)
        _, image = camera.read()
        now = datetime.datetime.utcnow()
        filename = now.strftime("%Y-%m-%d_%H-%M-%S-%f") + ".jpg"
        abs_filepath = settings.OPEN_SOURDOUGH_ROOT_IMAGE_DIR / str(self.session_id) / filename
        abs_filepath.mkdir(parents=True, exist_ok=True)
        cv2.imwrite(str(abs_filepath), image)
        with models.session_factory() as session:
            session.add(models.SourDoughImages(filename, now, self.session_id))
            session.commit()
            session.close()


if __name__ == "__main__":
    SourDoughMonitor(
        session_time=datetime.timedelta(minutes=1),
    ).start_session()
