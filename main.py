from itslearning_auto_logger.logger import login_to_itslearning, open_calendar_list_view, open_self_registration, crack_registration_code
from selenium_driver.driver import driver

def main():
    print('Auto logger engaging...')
    login_to_itslearning(driver)
    open_calendar_list_view(driver) 
    open_self_registration(driver)
    # crack_registration_code(driver)
    

if __name__ == '__main__':
    main()