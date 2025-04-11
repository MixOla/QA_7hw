import time

from pages.demoqa_page import DemoQa
from pages.elements_page import ElementsPage


def test_check_text(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    assert demo_qa_page.footer.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'


def test_check_text_centre(browser):
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)
    demo_qa_page.visit()
    demo_qa_page.btn_element.click()
    time.sleep(3)
    assert elements_page.btn_centre_element.get_text() == 'Please select an item from left to start practice.'


