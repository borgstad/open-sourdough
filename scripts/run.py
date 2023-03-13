import datetime
import time

import open_sourdough_monitor.main


def run_every_min():
    session_time = datetime.timedelta(hours=8)
    picture_interval = datetime.timedelta(minutes=1)
    open_sourdough_monitor.main.SourDoughMonitor(
        session_time=session_time, picture_interval=picture_interval
    ).start_session()


if __name__ == "__main__":
    run_every_min()
