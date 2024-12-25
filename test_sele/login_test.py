import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from navigation import go_to_sign_in_page

# Fixture to initialize and close the browser driver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

#TC01: Đăng nhập thành công
def test_valid_login(driver):
    go_to_sign_in_page(driver)
    driver.find_element(By.ID, "email").send_keys("hai6060@gmail.com")
    driver.find_element(By.ID, "password").send_keys("12345")
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    
    WebDriverWait(driver, 10).until(EC.url_to_be("http://localhost/PHP_E_Commerce_Web_Application_MySQL/bookshop/home.php"))
    assert driver.current_url == "http://localhost/PHP_E_Commerce_Web_Application_MySQL/bookshop/home.php"
    time.sleep(3)
    
#TC02: Nhập sai mật khẩu
def test_invalid_login(driver):
    go_to_sign_in_page(driver)
    driver.find_element(By.ID, "email").send_keys("alexson6060@gmail.com")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    
    time.sleep(3)
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "message"))
    )
    # Kiểm tra nội dung thông báo lỗi
    assert error_message.text == "Invalid username or password"

#TC03: Bỏ trống email và password
def test_empty_user_pass(driver):
    go_to_sign_in_page(driver)
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    time.sleep(3)
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "message"))
    )
    # Kiểm tra nội dung thông báo lỗi
    assert error_message.text == "Please enter your Email !!!"
    
#TC04: Điều hướng đến trang đăng ký
def test_redirect_to_register(driver):
    go_to_sign_in_page(driver)
    driver.find_element(By.LINK_TEXT, "Haven't account? Sign Up").click()
    time.sleep(3)
    assert driver.current_url == "http://localhost/PHP_E_Commerce_Web_Application_MySQL/bookshop/signUp.php"


    
   
 
    
       

    
