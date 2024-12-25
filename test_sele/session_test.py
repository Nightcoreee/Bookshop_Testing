import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from navigation import login
from navigation import go_to_sign_in_page

# Fixture to initialize and close the browser driver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_session_timeout(driver):
    login(driver, "hai6060@gmail.com", "12345")
    
    # Mở một tab mới và điều hướng đến trang đăng nhập
    driver.execute_script("window.open('http://localhost/PHP_E_Commerce_Web_Application_MySQL/bookshop/signIn.php', '_blank');")
    
    # Chuyển sang tab mới
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
     # Assert rằng URL hiện tại là trang chủ
    assert driver.current_url == "http://localhost/PHP_E_Commerce_Web_Application_MySQL/bookshop/home.php", "URL hiện tại không phải là trang chủ"
    time.sleep(2)