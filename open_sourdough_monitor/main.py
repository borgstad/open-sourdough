import datetime
import time

import cv2

from open_sourdough_monitor import models, settings, log

logger = log.logger


class SourDoughMonitor:
    def __init__(
        self,
        session_time: datetime.timedelta,
        picture_interval: datetime.timedelta = datetime.timedelta(minutes=1),
    ):
        self.session_id = models.get_latest_id() + 1
        self.session_end_time = datetime.datetime.now() + session_time
        self.picture_interval = picture_interval
        self.abs_filepath = settings.OPEN_SOURDOUGH_ROOT_IMAGE_DIR / str(
            self.session_id
        )

    def start_session(self):
        self.abs_filepath.mkdir(parents=True, exist_ok=True)
        while datetime.datetime.now() < self.session_end_time:
            self.take_picture()
            time.sleep(self.picture_interval.total_seconds())

    def take_picture(self):
        camera = cv2.VideoCapture(0)
        _, image = camera.read()
        now = datetime.datetime.utcnow()
        filename = now.strftime("%Y-%m-%d_%H-%M-%S-%f") + ".jpg"
        cv2.imwrite(str(self.abs_filepath / filename), image)
        logger.info(f"saved image: {self.abs_filepath / filename}")
        with models.session_factory() as session:
            session.add(models.SourDoughImages(filename, now, self.session_id))
            session.commit()
            session.close()
