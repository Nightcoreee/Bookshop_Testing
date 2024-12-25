import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from navigation import go_to_sign_up_page

# Fixture to initialize and close the browser driver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

#TC01: Đăng ký tài khoản thành công
def test_register(driver):
    go_to_sign_up_page(driver)
    driver.find_element(By.ID, "fname").send_keys("Ngọc")
    driver.find_element(By.ID, "lname").send_keys("Hà")
    driver.find_element(By.ID, "email").send_keys("huhu6060@gmail.com")
    driver.find_element(By.ID, "mobile").send_keys("0751264259")
    driver.find_element(By.ID, "password").send_keys("12345")
    driver.find_element(By.ID, "password2").send_keys("12345")
    
    gender_select = Select(driver.find_element(By.ID, "gender"))
    gender_select.select_by_visible_text("Male") 
    
    driver.find_element(By.CLASS_NAME, "btn-danger").click()
    
     # Chờ cho đến khi trang chuyển đến trang đăng nhập
    WebDriverWait(driver, 10).until(EC.url_to_be("http://localhost/PHP_E_Commerce_Web_Application_MySQL/bookshop/signIn.php"))
    assert driver.current_url == "http://localhost/PHP_E_Commerce_Web_Application_MySQL/bookshop/signIn.php"
    time.sleep(4)

#TC02: Bỏ trống các trường
def test_empty_regis(driver):
    go_to_sign_up_page(driver)
    driver.find_element(By.CLASS_NAME, "btn-danger").click()
    
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "message"))
    )
    # Kiểm tra nội dung thông báo lỗi
    assert error_message.text == "Please enter your First Name !!!"
    time.sleep(3)
    
#TC03: Nhập sai định dạng email
def test_wrong_email(driver):
    go_to_sign_up_page(driver)
    driver.find_element(By.ID, "fname").send_keys("Ngọc")
    driver.find_element(By.ID, "lname").send_keys("Hà")
    
    #Nhập sai định dạng email
    driver.find_element(By.ID, "email").send_keys("dsad")
    
    driver.find_element(By.ID, "mobile").send_keys("0751264259")
    driver.find_element(By.ID, "password").send_keys("12345")
    driver.find_element(By.ID, "password2").send_keys("12345")
    
    driver.find_element(By.CLASS_NAME, "btn-danger").click()
    
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "message"))
    )
    # Kiểm tra nội dung thông báo lỗi
    assert error_message.text == "Invalid Email !!!"
    time.sleep(3)

#TC04: Nhập mật khẩu không đủ 5 ký tự
def test_fill_pass(driver):
    go_to_sign_up_page(driver)
    driver.find_element(By.ID, "fname").send_keys("Ngọc")
    driver.find_element(By.ID, "lname").send_keys("Hà")
    driver.find_element(By.ID, "email").send_keys("huhu6060@gmail.com")
    driver.find_element(By.ID, "mobile").send_keys("0751264259")
    driver.find_element(By.ID, "password").send_keys("1234")
    driver.find_element(By.ID, "password2").send_keys("1234")
    
    gender_select = Select(driver.find_element(By.ID, "gender"))
    gender_select.select_by_visible_text("Male") 
    
    driver.find_element(By.CLASS_NAME, "btn-danger").click()
    
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "message"))
    )
    # Kiểm tra nội dung thông báo lỗi
    assert error_message.text == "Password must be between 5 - 20 charcters"
    time.sleep(3)

#TC05: Đăng ký tài khoản đã tồn tại
def test_acc_exists(driver):
    go_to_sign_up_page(driver)
    driver.find_element(By.ID, "fname").send_keys("huihi")
    driver.find_element(By.ID, "lname").send_keys("huhu")
    driver.find_element(By.ID, "email").send_keys("hai6060@gmail.com")
    driver.find_element(By.ID, "mobile").send_keys("0781164259")
    driver.find_element(By.ID, "password").send_keys("12345")
    driver.find_element(By.ID, "password2").send_keys("12345")
    
    gender_select = Select(driver.find_element(By.ID, "gender"))
    gender_select.select_by_visible_text("Male") 
    
    driver.find_element(By.CLASS_NAME, "btn-danger").click()
    
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "message"))
    )
    # Kiểm tra nội dung thông báo lỗi
    assert error_message.text == "Email already exists."
    time.sleep(3)

#TC06: Nhập số điện thoại không hợp lệ
def test_invalid_mobile(driver):
    go_to_sign_up_page(driver)
    driver.find_element(By.ID, "fname").send_keys("huihi")
    driver.find_element(By.ID, "lname").send_keys("huhu")
    driver.find_element(By.ID, "email").send_keys("hihi6060@gmail.com")
    driver.find_element(By.ID, "mobile").send_keys("0981164259")
    driver.find_element(By.ID, "password").send_keys("12345")
    driver.find_element(By.ID, "password2").send_keys("12345")
    
    gender_select = Select(driver.find_element(By.ID, "gender"))
    gender_select.select_by_visible_text("Male") 
    
    driver.find_element(By.CLASS_NAME, "btn-danger").click()
    
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "message"))
    )
    # Kiểm tra nội dung thông báo lỗi
    assert error_message.text == "Invalid Mobile Number"
    time.sleep(4)

#TC07: Chuyển hướng đến trang đăng nhập
def test_redirect_to_login(driver):
    go_to_sign_up_page(driver)
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Already Registered? Sign In").click()
    
    # Chờ cho đến khi trang chuyển đến trang đăng nhập
    WebDriverWait(driver, 10).until(EC.url_to_be("http://localhost/PHP_E_Commerce_Web_Application_MySQL/bookshop/signIn.php"))
    assert driver.current_url == "http://localhost/PHP_E_Commerce_Web_Application_MySQL/bookshop/signIn.php"
    
    time.sleep(2)
