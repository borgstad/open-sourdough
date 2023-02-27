import time

import open_sourdough_monitor.main


def run_every_min():
    while True:
        open_sourdough_monitor.main.SourDoughMonitor().take_picture()
        time.sleep(60)


if __name__ == "__main__":
    run_every_min()
