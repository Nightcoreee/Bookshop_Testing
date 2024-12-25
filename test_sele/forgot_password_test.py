import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from navigation import autofill_login
from navigation import click_forgot_password
from navigation import click_reset_button_and_accept_alert
from navigation import go_to_sign_in_page
# Fixture to initialize and close the browser driver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


#TC01: Đổi mật khẩu thành công
def test_forgot_password(driver):
    autofill_login(driver, "alexson6060@gmail.com", "14232")
    click_forgot_password(driver)
    time.sleep(15)
    
    #nhập pass
    driver.find_element(By.ID, "np").send_keys("12345")
    driver.find_element(By.ID, "rnp").send_keys("12345")
    
    time.sleep(5)
    
    #Nhấn nút reset 
    click_reset_button_and_accept_alert(driver)
    
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys("12345")
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    
    WebDriverWait(driver, 10).until(EC.url_to_be("http://localhost/PHP_E_Commerce_Web_Application_MySQL/bookshop/home.php"))
    assert driver.current_url == "http://localhost/PHP_E_Commerce_Web_Application_MySQL/bookshop/home.php"
    time.sleep(3)

#TC02: Bỏ trống email rồi nhấn Forget Password
def test_forgot_password_empty_email(driver):
    go_to_sign_in_page(driver)
    
    driver.find_element(By.LINK_TEXT, "Forget Password?").click()
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "message"))
    )
    # Kiểm tra nội dung thông báo lỗi
    assert error_message.text == "Invalid Email Address"
    time.sleep(3)
    
#TC03: Nhập email chưa đăng ký
def test_forgot_password_email_has_no_regis(driver):
    go_to_sign_in_page(driver)
    
    driver.find_element(By.ID, "email").send_keys("alex6060@gmail.com")
    
    driver.find_element(By.LINK_TEXT, "Forget Password?").click()
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "message"))
    )
    # Kiểm tra nội dung thông báo lỗi
    assert error_message.text == "Invalid Email Address"
    time.sleep(3)

