from selenium.webdriver.common.by import By


class BasePage():
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def visit(self):
        return self.driver.get(self.base_url)


