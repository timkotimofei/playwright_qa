import pytest
from playwright.sync_api import Page, Playwright, ViewportSize


@pytest.fixture()
def driver(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context(
        viewport=ViewportSize(width=1440, height=980),
        base_url="https://www.qa-practice.com"
    )
    page = context.new_page()
    # page.set_default_timeout(5000) # изм. ожидания (т.к. из коробки = 30 сек)
    yield page
    page.close()
    context.close()
    browser.close()

@pytest.fixture()
def driver_saucedemo(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context(
        viewport=ViewportSize(width=1440, height=980),
        base_url="https://www.saucedemo.com/"
    )
    page = context.new_page()
    yield page
    page.close()
    context.close()
    browser.close()


@pytest.fixture()
def driver_demoqa(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context(
        viewport=ViewportSize(width=1480, height=1020),
        base_url="https://demoqa.com/"
    )
    page = context.new_page()
    yield page
    page.close()
    context.close()
    browser.close()

