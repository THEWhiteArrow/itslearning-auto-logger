from threading import Thread
from itslearning_auto_logger.logger import queue_for_presence
from selenium_driver.driver import drivers
from utils.toml_helper import config

def main():
    print('Auto logger engaging...')

    driver_main = drivers.get_driver('main')
    queue_for_presence(driver_main, inform_about_registration=True)

    for i in range(0, config['driver']['count']):
        driver = drivers.get_driver(f"driver{i}") 
        Thread(
            target=queue_for_presence, 
            args=( 
                driver,
                10*1000//15*i, 
                10*1000//15*(i+1), 
                2
            )
        ).start()
 

    
    

if __name__ == '__main__':
    main()