from typing import Dict
from selenium.webdriver import Chrome, Safari, Firefox, Ie, Edge
from selenium.webdriver.chrome.options import Options
from utils.toml_helper import config


class DriverWrapper(Chrome,Safari,Firefox,Ie,Edge):
 
    def __init__(self):
        self.drivers : Dict = {}
    
    def _create_driver(self, id:str):
        if config['driver']['browser'] == 'chrome':
            options = Options()
            if config['driver']['headless'] :
                options.add_argument("--headless")
            self.drivers[id] = Chrome(options=options)

        elif config['driver']['browser'] == 'safari':
            self.drivers[id] = Safari()
        elif config['driver']['browser'] == 'firefox':
            self.drivers[id] = Firefox()
        elif config['driver']['browser'] == 'ie':
            self.drivers[id] = Ie()
        elif config['driver']['browser'] == 'edge':
            self.drivers[id] = Edge()
        else:
            raise Exception('Browser not supported')

    def get_driver(self, id:str):
        if id not in self.drivers:
            self._create_driver(id)
        return self.drivers[id]

drivers = DriverWrapper()

 
