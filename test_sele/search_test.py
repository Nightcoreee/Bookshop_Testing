import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from navigation import go_to_home_page
from navigation import check_product_title

# Fixture to initialize and close the browser driver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
    
#TC01: Tìm sản phẩm theo tên và theo All Categories
def test_search(driver):
    go_to_home_page(driver)
    driver.find_element(By.ID, "basic_search_txt").send_keys("Mechanical Science")
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.mt-1.mb-1").click()
    time.sleep(3)
    # Kiểm tra sản phẩm
    check_product_title(driver, "Mechanical Science")
    time.sleep(3)
    
#TC02: Tìm sản phẩm khi tắt tên sản phẩm và chọn All Categories
def test_search_abbreviate(driver):
    go_to_home_page(driver)
    driver.find_element(By.ID, "basic_search_txt").send_keys("Mechanic")
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.mt-1.mb-1").click()
    time.sleep(3)
    # Kiểm tra sản phẩm
    check_product_title(driver, "Mechanical Science")
    time.sleep(3)
    
    
#TC03: Tìm sản phẩm đúng tên và thêm khoảng trắng
def test_search_white_space(driver):
    go_to_home_page(driver)
    driver.find_element(By.ID, "basic_search_txt").send_keys("Mechanical Science    ")
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.mt-1.mb-1").click()
    time.sleep(3)
    # Kiểm tra sản phẩm
    check_product_title(driver, "Mechanical Science")
    time.sleep(3)

#TC04: Nhập ký tự đặc biệt
def test_search_empty(driver):
    go_to_home_page(driver)
    driver.find_element(By.ID, "basic_search_txt").send_keys("@#$^%&")
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.mt-1.mb-1").click()
    time.sleep(3)

#TC05: Nhập số (trường hợp có sản phẩm chứa số ví dụ: Physics Paper Rewiew 2020)
def test_search_number(driver):
    go_to_home_page(driver)
    driver.find_element(By.ID, "basic_search_txt").send_keys("2020") 
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.mt-1.mb-1").click()
    time.sleep(3)
    # Kiểm tra sản phẩm
    check_product_title(driver, "Physics Paper Rewiew 2020")
    time.sleep(3) 

#TC06: Nhập số ngẫu nhiên
def test_search_number_random(driver):
    go_to_home_page(driver)
    driver.find_element(By.ID, "basic_search_txt").send_keys("123456789")
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.mt-1.mb-1").click()
    time.sleep(3) 
    
#TC07: Tìm sản phẩm theo mọi thể loại và kiểm tra
def search_by_category(driver, category, expected_title):
    go_to_home_page(driver)
    driver.find_element(By.ID, "basic_search_txt").send_keys("Mechanical Science")
    
    category_select = Select(driver.find_element(By.ID, "basic_search_select"))
    category_select.select_by_visible_text(category)
    
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.mt-1.mb-1").click()
    time.sleep(3)
    # Kiểm tra sản phẩm
    check_product_title(driver, "Mechanical Science")
    
    # Sử dụng dữ liệu tham số để kiểm tra từng thể loại
@pytest.mark.parametrize("category, expected_title", [
        ("Novels", "Some Novel Title"),
        ("Short Stories", "Some Short Story Title"),
        ("Language", "Some Language Title"),
        ("Religion", "Some Religion Title"),
        ("Translations", "Some Translation Title"),
])

def test_search_by_category(driver, category, expected_title):
    search_by_category(driver, category, expected_title)
        