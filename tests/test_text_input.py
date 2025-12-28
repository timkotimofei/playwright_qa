import time
from playwright.sync_api import expect


def test_empty_field(text_input_page):
    text_input_page.open()
    text_input_page.click_input_field()
    text_input_page.press_enter()
    assert text_input_page.evaluate_empty_field_submit() == 'Please fill out this field.'


def test_typing_text_field(text_input_page):
    text_input_page.open()
    text_input_page.click_input_field()
    text_input_page.typing_in_a_input_field('Timofei')
    text_input_page.press_enter()
    time.sleep(5)





