from playwright.sync_api import Page

class TextInputPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto("https://www.qa-practice.com/elements/input/simple")

