import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from navigation import go_to_sign_in_page
from navigation import login
# Fixture to initialize and close the browser driver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
    
def test_logout(driver):
    login(driver, "hai6060@gmail.com", "12345")
    time.sleep(3)
     # Nhấp vào nút dropdown
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "dropdown-toggle"))
    ).click()
    
    # Thực hiện đăng xuất
    signout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@class='dropdown-item' and text()='Signout']"))
    )
    signout_button.click()
    
    WebDriverWait(driver, 10).until(EC.url_to_be("http://localhost/PHP_E_Commerce_Web_Application_MySQL/bookshop/home.php"))
    assert driver.current_url == "http://localhost/PHP_E_Commerce_Web_Application_MySQL/bookshop/home.php"
    
    time.sleep(3)