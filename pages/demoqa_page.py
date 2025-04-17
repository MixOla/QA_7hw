from components.components import WebElement
from pages.base_page import BasePage


class DemoQa(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)

        self.footer = WebElement(driver, '#app > footer > span')
        self.btn_element = WebElement(driver,
                                      '#app > div > div > div.home-body > div > div:nth-child(1)')
