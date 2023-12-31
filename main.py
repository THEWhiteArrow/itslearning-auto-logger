from threading import Thread
import time
from itslearning_auto_logger.logger import queue_for_presence
from selenium_driver.driver import drivers
from utils.toml_helper import config


def create_in_threads():
    for i in range(0, config["driver"]["count"]):
        driver = drivers.get_driver(f"thread_driver{i}")
        Thread(
            target=queue_for_presence,
            args=(
                driver,
                10 * 1000 // 15 * i,
                10 * 1000 // 15 * (i + 1),
                config["driver"]["repeat"],
            ),
        ).start()


def main():
    """
    This is the main function of the program. It loads the drivers, wait for registration to open and starts the threads.
    It has to phases. First phase is to wait for registration to open. Second phase is to crack the registration code.
    """
    print("Auto logger engaging...")

    driver_main = drivers.get_driver("main")
    queue_for_presence(driver_main, inform_about_registration=True)
    create_in_threads()


if __name__ == "__main__":
    main()
