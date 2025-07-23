import time
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import *


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def login_naukri(driver, username, password):
    driver.get(Base_URL)
    login_btn = driver.find_element(By.LINK_TEXT, "Login")
    login_btn.click()
    time.sleep(2)
    email_input = driver.find_element(By.XPATH, user_xpath)
    email_input.send_keys(username)
    password_input = driver.find_element(By.XPATH, pwd_xpath)
    password_input.send_keys(password)
    submit_btn = driver.find_element(By.XPATH, login_button_xpath)
    submit_btn.click()
    time.sleep(5)
    driver.get(profile_url)
    edit_icon = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, user_name_edit_icon_xpath)))
    edit_icon.click()
    print("Clicked edit icon successfully.")
    time.sleep(2)
    first_name_input = driver.find_element(By.XPATH, first_name_input_xpath)
    first_name_input.clear()
    first_name_input.send_keys(new_username)
    save_button = driver.find_element(By.XPATH, save_button_xpath)
    save_button.click()
    print("Saved first name successfully.")
    time.sleep(5)


    return "My Naukri" in driver.page_source

def test_login_naukri(driver):
    USERNAME = email
    PASSWORD = pwd
    login_naukri(driver, USERNAME, PASSWORD), "Login failed."