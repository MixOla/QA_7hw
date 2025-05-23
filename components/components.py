from selenium.webdriver.common.by import By


class WebElement():
    def __init__(self, driver, locator=''):
        self.driver = driver
        self.locator = locator



    def find_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def find_elements(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.locator)

    def click(self):
        return self.find_element().click()

    def get_text(self):
        return str(self.find_element().text)

    def visible(self):
        return self.find_element().is_displayed()

    def check_count_elements(self, count: int) -> bool:
        return True if len(self.find_elements()) == count else False


