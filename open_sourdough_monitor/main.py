import datetime
import time
from pathlib import Path

import cv2
import numpy as np

from open_sourdough_monitor import log, models, settings

logger = log.logger


class SourDoughMonitor:
    """
    A class representing a sourdough monitor that takes pictures at regular intervals
    and stores them in a directory.
    """

    def __init__(
        self,
        session_time: datetime.timedelta,
        picture_interval: datetime.timedelta = datetime.timedelta(minutes=1),
    ) -> None:
        """
        Initializes a new instance of the `SourDoughMonitor` class.

        :param session_time: The total duration of the session.
        :param picture_interval: The interval between two consecutive pictures.
        """
        self.session_id = models.get_latest_id() + 1
        self.session_end_time = datetime.datetime.now() + session_time
        self.picture_interval = picture_interval
        self.abs_filepath = settings.OPEN_SOURDOUGH_ROOT_IMAGE_DIR / str(
            self.session_id
        )

    def start_session(self) -> None:
        """
        Starts the sourdough monitoring session by taking pictures at regular intervals
        until the session end time is reached.
        """
        self.abs_filepath.mkdir(parents=True, exist_ok=True)
        while datetime.datetime.now() < self.session_end_time:
            camera = cv2.VideoCapture("/dev/video0")
            success, image = camera.read()
            camera.release()
            if not success:
                logger.error("failed to read image from camera")
                continue
            self.register_image(image)
            time.sleep(self.picture_interval.total_seconds())

    def register_image(self, image: np.ndarray) -> None:
        """
        Takes a picture and saves it to the designated directory.

        :param image: The image to be saved.
        """
        now = datetime.datetime.utcnow()
        filename = now.strftime("%Y-%m-%d_%H-%M-%S-%f") + ".jpg"
        file_path = self.abs_filepath / filename

        cv2.imwrite(str(file_path), image)
        logger.info(f"saved image: {file_path}")

        with models.session_factory() as session:
            image_entry = models.SourDoughImages(filename, now, self.session_id)
            session.add(image_entry)
            session.commit()
            logger.info(f"added image to database: {image_entry}")
