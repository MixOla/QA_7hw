from pages.demoqa_page import DemoQa
from pages.modal_dialogs import ModalDialogs


def test_modal_elements(browser):
    modal_dialogs = ModalDialogs(browser)
    modal_dialogs.visit()
    assert modal_dialogs.elements.check_count_elements(count=5)

def test_navigation_modal(browser):
    modal_dialogs = ModalDialogs(browser)
    demoqa_page = DemoQa(browser)
    modal_dialogs.visit()
    browser.refresh()
    modal_dialogs.icon_main_page.click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    assert demoqa_page.check_base_url()
    assert demoqa_page.check_title('DEMOQA')
    browser.set_window_size(1000, 1000)
