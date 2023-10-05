import time
import asyncio
from typing import List
# SELENIUM
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.remote.webelement import WebElement

# TOML_FILE
PATH = "./chromedriver.exe"
LOGIN = "<>"
PASSWORD = "<>"
DELAY = 1

# SETUP
driver = webdriver.Chrome()


 
  
# async def zaloguj(login, password):

#     link = driver.find_element_by_link_text('zaloguj się')
#     link.click()

#     inputUsername = driver.find_element_by_id('input_username')
#     inputPassword = driver.find_element_by_id('input_password')
#     inputUsername.send_keys(login)
#     inputPassword.send_keys(password)

#     loginBtn = driver.find_element_by_class_name('login_btn')
#     loginBtn.click()

#     #  rejectCookies()
#     #  steamQuardBtn = driver.find_element_by_id('twofactorcode_entry')
#     #  steamQuardBtn.send_keys(Keys.RETURN)
#     #  time.sleep(3)
# async def confirmPositiveLogging():
#     isLoggedIn = False
#     while isLoggedIn == False:
#         if len(driver.find_elements_by_class_name('persona_name_text_content')) != 0:
#             isLoggedIn = True
#         else:
#             time.sleep(1)
#     time.sleep(3)
# async def sortuj():
#     time.sleep(5)
#     sortBtn = driver.find_element_by_id('csgofloat_sort_by_float')
#     sortAmountSelect = driver.find_element_by_id('pageSize')
#     sortAmountSelect.click()
#     sortOption = driver.find_element(By.XPATH, '//option[@value="100"]')
#     sortOption.click()

#     time.sleep(1)
#     sortBtn.click()
#     time.sleep(1)
# async def przeszukaj(p, f, a):
#     global soldTextFragment
#     itemRows = driver.find_elements_by_css_selector(
#         '.market_recent_listing_row')

#     n = 0
#     boughtSkin = False

#     for row in itemRows:
#         itemPrice = row.find_elements_by_css_selector(
#             '.market_listing_price.market_listing_price_with_fee')

#         if len(itemPrice) > 0 and boughtSkin == False:
#             price = 1000000
#             if itemPrice[0].text[:4] != soldTextFragment:
#                 price = float(itemPrice[0].text[:-DELAY].replace(',', '.'))

#             global firstAmount
#             global secondAmount
#             targetedAmount = 0

#             if a == 'firstAmount':
#                 targetedAmount = firstAmount
#             else:
#                 targetedAmount = secondAmount

#             if price <= p and targetedAmount > 0:

#                 itemFloat = float(row.find_element_by_css_selector(
#                     '.csgofloat-itemfloat').text[7:])
#                 if itemFloat <= f:
#                     await kup(n, a)
#                     boughtSkin = True
#                     print('##################')
#                     print(numberOfBoughtSkins)
#                     print(price)
#                     print(itemFloat)
#         n += 1
# async def kup(n, a):
#     global buyingBtnText
#     buyBtns = driver.find_elements_by_link_text(buyingBtnText)
#     buyBtns[n].click()
#     time.sleep(DELAY)
#     global checkboxWasUsed
#     global numberOfBoughtSkins
#     global firstAmount
#     global secondAmount

#     if checkboxWasUsed == False:
#         checkbox = driver.find_element_by_id(
#             'market_buynow_dialog_accept_ssa_label')
#         checkbox.click()
#         checkboxWasUsed = True

#     purchaseBtn = driver.find_element_by_id('market_buynow_dialog_purchase')
#     purchaseBtn.click()
#     time.sleep(11)

#     stillPurchaseBtn = driver.find_elements_by_id(
#         'market_buynow_dialog_purchase')
#     if len(stillPurchaseBtn) == 0:
#         numberOfBoughtSkins += 1
#         if a == 'firstAmount':
#             firstAmount -= 1
#         else:
#             secondAmount -= 1
# async def botServing():
#     global numberOfBoughtSkins
#     global numberOfWantedSkins
#     global checkboxWasUsed
#     global length

#     while numberOfBoughtSkins < numberOfWantedSkins:
#         for i in range(length):
#             if numberOfBoughtSkins < numberOfWantedSkins:
#                 driver.get(href[i])
#                 await sortuj()
#                 await przeszukaj(maxPrice[i], maxFloat[i], amount[i])
#                 time.sleep(15)
#                 checkboxWasUsed = False



async def login():
    driver.get("https://via.itslearning.com/")
    time.sleep(DELAY)
    driver.find_element(by=By.LINK_TEXT, value='VIA-login').click()
    time.sleep(DELAY)
        
    driver.find_element(by=By.ID, value='login').send_keys(LOGIN)
    driver.find_element(by=By.ID, value='passwd').send_keys(PASSWORD)
    driver.find_element(by=By.ID, value='nsg-x1-logon-button').click()
    time.sleep(DELAY)

async def open_calendar():
    driver.get('https://via.itslearning.com/Calendar/Schedule.aspx')
    time.sleep(DELAY)

async def get_events() -> List[WebElement]:
    events = driver.find_elements(by=By.CLASS_NAME, value='fc-event-inner')
    time.sleep(DELAY)
    return events
 
def parse_number_to_password(number):
    number = str(number)
    if len(number) < 4:
        number = "0" * (4 - len(number)) + number
    return number

async def find_button():
    schedule = driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Schedule')]")
    list_view = driver.find_element(by=By.XPATH, value="//*[contains(text(), 'List')]")
    list_view.click()
    
    
    button1 = driver.find_elements(by=By.XPATH, value="//*[contains(text(), 'Register presence')]")
    button2 = driver.find_elements(by=By.CSS_SELECTOR, value='button.ccl-button.ccl-button-color-green')
    
    button1[0].click()
    time.sleep(DELAY)

    input_field2 = driver.find_element(by=By.ID, value='code')
    input_field2.click()
    time.sleep(DELAY)
    actions = webdriver.ActionChains(driver)
    
    starting_number = 5400
    for i in range(starting_number,10*1000):
        actions.send_keys('\b\b\b\b')
        actions.send_keys(parse_number_to_password(i))
        actions.perform()

    pass
    

async def via_logger():
    # GETTING ON PAGE AND LOGGING
    # driver.get(href[0])
    # await zaloguj(userLogin, userPassword)
    # await confirmPositiveLogging()
    # await botServing()
    await login()
    await open_calendar()
    
    await find_button()
     
    

    time.sleep(60)


 


# ASYNC LOOP EVENT
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(via_logger())
    loop.close() 