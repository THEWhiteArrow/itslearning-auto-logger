import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium_driver.driver import DriverWrapper
from selenium.webdriver.remote.webelement import WebElement 

from utils.toml_helper import config
from utils.utils import parse_number_to_password

def wait_for_element(driver : DriverWrapper, by : By, value : str, timeout : int = 20, refresh : bool = False) -> WebElement:
    """
    Waits for the element to appear on the page. 
    @param driver: The selenium driver.
    @param by: The selector type.
    @param value: The selector value.
    @param timeout: The timeout in seconds. If negative, it will wait forever (until some lower bound).
    @param refresh: If True, the page will be refreshed every second.
    @return WebElement: The element.
    """

    while timeout > 0 or (timeout < 0 and timeout > -60*60*24):
        try:
            
            element = driver.find_element(by=by, value=value)
            return element
        except Exception as e:
            if refresh:
                driver.refresh()
                time.sleep(2)
            else:
                time.sleep(1)
            timeout -= 1

    raise Exception('Element not found')

def queue_for_presence(driver : DriverWrapper, code_start : int = 0 , code_end : int = 10*1000 , repeat : int = 1, inform_about_registration : bool = False) -> bool:
    """
    Completes one cycle of logging in and registering for presence.
    @param driver: The selenium driver.
    @param code_start: The start of the code range.
    @param code_end: The end of the code range.
    @param repeat: How many times to repeat the cycle.
    @param inform_about_registration: If True, the function will return after opening the self registration page.
    @return bool: True if the registration has started, False if it has not.
    """

    print("Logging in")
    login_to_itslearning(driver)
    print("Opening calendar list view")
    open_calendar_list_view(driver) 
    print("Opening self registration")
    open_self_registration(driver)
    if inform_about_registration:
        print("Registration started")
        return True
    print("Cracking registration code")
    crack_registration_code(driver, code_start, code_end, repeat)
    return False

def login_to_itslearning(driver : DriverWrapper):
    """
    Logs in to itslearning.
    @param driver: The selenium driver.
    """

    driver.get("https://via.itslearning.com/")
    wait_for_element(driver, By.LINK_TEXT, 'VIA-login').click() 
    wait_for_element(driver, By.ID, 'login').send_keys( config["via"]["login"] )
    wait_for_element(driver, By.ID, 'passwd').send_keys( config["via"]["password"] )
    wait_for_element(driver, By.ID, 'nsg-x1-logon-button').click()
    wait_for_element(driver, By.ID, "pm-user-status-image")

def open_calendar_list_view(driver : DriverWrapper):
    """
    Opens the calendar list view.
    @param driver: The selenium driver.
    """

    driver.get('https://via.itslearning.com/Calendar/Schedule.aspx')
    wait_for_element(driver, By.XPATH, "//*[contains(text(), 'List')]").click()
    wait_for_element(driver, By.ID, 'ctl00_PageHeader_TT')

def open_self_registration(driver : DriverWrapper): 
    """
    Opens the self registration page.
    @param driver: The selenium driver.
    """

    driver.get('https://via.itslearning.com/Calendar/Schedule.aspx')
    wait_for_element(driver, By.CSS_SELECTOR, 'button.ccl-button.ccl-button-color-green[aria-label="Register presence"]', refresh=True, timeout=-1).click()
    
    # --- This is a hack ---
    # --- There are two elements with the same text so that is why i select other text ---
    # wait_for_element(driver, By.XPATH, "//*[contains(text(), 'SELF-REGISTRATION')]",timeout=-1, refresh=True)
    # wait_for_element(driver, By.XPATH, "//*[contains(text(), 'Register presence')]").click()


def crack_registration_code(driver : DriverWrapper, code_start:int = 0, code_end:int = 10*1000, repeat : int = 1):
    """
    Cracks the registration code.
    @param driver: The selenium driver.
    @param code_start: The start of the code range.
    @param code_end: The end of the code range.
    @param repeat: How many times to repeat the cycle.
    """
    
    wait_for_element(driver, By.ID, 'code').click()

    actions = ActionChains(driver)
    for r in range(0,repeat):
        for i in range(code_start,code_end):
            actions.send_keys('\b\b\b\b' + parse_number_to_password(i))
            actions.perform()

 