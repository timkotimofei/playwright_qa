
def test1(driver):
    driver.goto("/elements/input/simple")
    input_field = driver.locator("//input[@name='text_string']")
    result_area = driver.locator("//div[@class='result']")
    text = "12345"
    input_field.fill(text)
    input_field.press('Enter')
    assert text in result_area.all_text_contents()[0]


def test2(driver_saucedemo):
    driver_saucedemo.goto("")
    user_name = "//input[@id='user-name']"
    password = "//input[@id='password']"
    login_button = "//input[@id='login-button']"

    driver_saucedemo.locator(user_name).fill('standard_user')
    driver_saucedemo.locator(password).fill('secret_sauce')
    driver_saucedemo.locator(login_button).click()


def test_radio_button_yes(driver_demoqa):
    driver_demoqa.goto(
        url="radio-button",
        wait_until="domcontentloaded"
    )
    radio_button_yes = "label[for='yesRadio']"
    text_status = "span[class='text-success']"

    driver_demoqa.locator(radio_button_yes).check()
    text = driver_demoqa.locator(text_status).text_content()

    assert text == "Yes"






