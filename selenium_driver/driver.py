from selenium.webdriver import Chrome, Safari, Firefox, Ie, Edge
from utils.toml_helper import config

class DriverWrapper(Chrome,Safari,Firefox,Ie,Edge):
    def __init__(self):
        if config['driver']['browser'] == 'chrome':
            self.driver = Chrome()
        elif config['driver']['browser'] == 'safari':
            self.driver = Safari()
        elif config['driver']['browser'] == 'firefox':
            self.driver = Firefox()
        elif config['driver']['browser'] == 'ie':
            self.driver = Ie()
        elif config['driver']['browser'] == 'edge':
            self.driver = Edge()
        else:
            raise Exception('Browser not supported')
    def get_driver(self):
        return self.driver

driver = DriverWrapper().get_driver()

 
