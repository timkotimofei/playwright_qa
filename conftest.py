import pytest
from pages.text_input_page import TextInputPage



@pytest.fixture()
def text_input_page(page):
    return TextInputPage(page)






