from selenium.webdriver.common.by import By


class BasePage():
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def visit(self):
        return self.driver.get(self.base_url)

    def back(self):
        return self.driver.back()

    def forward(self):
        return self.driver.forward()

    def refresh(self):
        return self.driver.refresh()

    def check_base_url(self):
        return True if self.driver.current_url == self.base_url else False

    def check_title(self, title):
        return True if self.driver.title == title else False
