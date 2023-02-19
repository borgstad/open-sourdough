import open_sour_dough_monitor.main
import time


def run_every_min():
    while True:
        open_sour_dough_monitor.main.SourDoughMonitor().take_picture()
        time.sleep(60)


if __name__ == "__main__":
    run_every_min()
