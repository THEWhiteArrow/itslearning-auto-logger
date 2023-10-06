import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium_driver.driver import DriverWrapper
from selenium.webdriver.remote.webelement import WebElement 

from utils.toml_helper import config
from utils.utils import parse_number_to_password

def wait_for_element(driver : DriverWrapper, by : By, value : str, timeout : int = 10, refresh : bool = False) -> WebElement:
    while timeout > 0 or (timeout < 0 and timeout > -60*60*24):
        try:
            element = driver.find_element(by=by, value=value)
            return element
        except Exception as e:
            print(e.__str__())
            time.sleep(1)
            timeout -= 1
            if refresh:
                driver.refresh()
    raise Exception('Element not found')

def queue_for_presence(driver : DriverWrapper, code_start : int = 0 , code_end : int = 10*1000 , repeat : int = 1, inform_about_registration : bool = False):
    login_to_itslearning(driver)
    open_calendar_list_view(driver) 
    open_self_registration(driver)
    if inform_about_registration:
        print("Registration started")
        return True
    crack_registration_code(driver)
    return False

def login_to_itslearning(driver : DriverWrapper):
    driver.get("https://via.itslearning.com/")
    wait_for_element(driver, By.LINK_TEXT, 'VIA-login').click() 
    wait_for_element(driver, By.ID, 'login').send_keys( config["via"]["login"] )
    wait_for_element(driver, By.ID, 'passwd').send_keys( config["via"]["password"] )
    wait_for_element(driver, By.ID, 'nsg-x1-logon-button').click()
    wait_for_element(driver, By.ID, "pm-user-status-image")

def open_calendar_list_view(driver : DriverWrapper):
    driver.get('https://via.itslearning.com/Calendar/Schedule.aspx')
    wait_for_element(driver, By.XPATH, "//*[contains(text(), 'List')]").click()
    wait_for_element(driver, By.ID, 'ctl00_PageHeader_TT')

def open_self_registration(driver : DriverWrapper): 
    driver.get('https://via.itslearning.com/Calendar/Schedule.aspx')
    
    # --- This is a hack ---
    # --- There are two elements with the same text so that is why i select other text ---
    # wait_for_element(driver, By.XPATH, "//*[contains(text(), 'SELF-REGISTRATION')]",timeout=-1, refresh=True)
    # wait_for_element(driver, By.XPATH, "//*[contains(text(), 'Register presence')]").click()

    wait_for_element(driver, By.CSS_SELECTOR, 'button.ccl-button.ccl-button-color-green[aria-label="Register presence"]', refresh=True, timeout=-1).click()

def crack_registration_code(driver : DriverWrapper):
    wait_for_element(driver, By.ID, 'code').click()

    actions = ActionChains(driver)
    for i in range(0,10*1000):
        actions.send_keys('\b\b\b\b' + parse_number_to_password(i))
        actions.perform()

 