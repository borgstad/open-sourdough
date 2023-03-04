import datetime
import time

import open_sourdough_monitor.main


def run_every_min():
    session_time = datetime.timedelta(minutes=1)
    picture_interval = datetime.timedelta = datetime.timedelta(seconds=5)
    open_sourdough_monitor.main.SourDoughMonitor(
        session_time=session_time, picture_interval=picture_interval
    ).start_session()


if __name__ == "__main__":
    run_every_min()
