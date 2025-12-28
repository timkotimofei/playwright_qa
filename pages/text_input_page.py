from playwright.sync_api import Page

class TextInputPage:
    def __init__(self, page: Page):
        self.page = page
        self.text_input_field = page.get_by_role("textbox", name="Text string*")

    def open(self):
        self.page.goto("https://www.qa-practice.com/elements/input/simple")

    def click_input_field(self):
        self.text_input_field.click()

    def press_enter(self):
        self.text_input_field.press("Enter")

    def typing_in_a_input_field(self, text):
        self.text_input_field.fill(text)

    def evaluate_empty_field_submit(self):
        return self.text_input_field.evaluate("el => el.validationMessage")



