import time

from pages.accordian import Accordian


def test_visible_accordian(browser):
    accordian_page = Accordian(browser)
    accordian_page.visit()
    assert accordian_page.element_1.visible()
    accordian_page.element_2.click()
    time.sleep(2)
    assert not accordian_page.element_1.visible()

def test_visible_accordion_default(browser):
    accordian_page = Accordian(browser)
    accordian_page.visit()
    assert not accordian_page.element_3.visible()
    assert not accordian_page.element_4.visible()
    assert not accordian_page.element_5.visible()
