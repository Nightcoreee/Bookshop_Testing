import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from navigation import login
from navigation import check_product_title_wl
from navigation import open_dropdown_and_click_watchlist
from navigation import click_buy_now
from navigation import click_add_to_watchlist

# Fixture to initialize and close the browser driver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
    
#TC01: Thêm sản phẩm vào wl và kiểm tra nó 
def test_wl_pro(driver):
    login(driver, "hai6060@gmail.com", "12345")
    #Scroll xuống dưới 1600px
    driver.execute_script("window.scrollBy(0, 1600);")
    time.sleep(2)
    
    add_to_wishlist_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "heart18"))
    )
    add_to_wishlist_button.click()
    
    time.sleep(2)
    #Scroll lên trên 1600px
    driver.execute_script("window.scrollBy(0, -1600);")
    time.sleep(2)
    
    # Mở dropdown và chọn wishlist
    open_dropdown_and_click_watchlist(driver)
    
    # Kiểm tra sản phẩm
    check_product_title_wl(driver, "Thummanhandiya")
    time.sleep(2)
    
    
#TC02: Thêm sản phẩm vào wl thông qua Buy Now
def test_wl_as_bn(driver):
    login(driver, "hai6060@gmail.com", "12345")
    #Scroll xuống dưới 1600px
    driver.execute_script("window.scrollBy(0, 1600);")
    time.sleep(2)
    
    #Nút Buy Now
    click_buy_now(driver)
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "btn-light").click()
    
    time.sleep(2)
     # Mở dropdown và chọn wishlist
    open_dropdown_and_click_watchlist(driver)
    
    # Kiểm tra sản phẩm
    check_product_title_wl(driver, "Thummanhandiya")
    time.sleep(2)

#TC03: Bỏ sản phẩm khỏi wl thông qua Watchlist
def test_rm_pro_wl(driver):
    login(driver, "hai6060@gmail.com", "12345")
    
    # Mở dropdown và chọn wishlist
    open_dropdown_and_click_watchlist(driver)
    
    # Kiểm tra sản phẩm
    check_product_title_wl(driver, "Thummanhandiya")
    driver.find_element(By.CLASS_NAME, "btn-danger").click()
    time.sleep(2)

#TC04: Bỏ sản phẩm khỏi wl thông qua trang sản phẩm
def test_rm_pro_fanpage(driver):
    login(driver, "hai6060@gmail.com", "12345")
    
    driver.execute_script("window.scrollBy(0, 1600);")
    time.sleep(2)
    
    # Gọi hàm để nhấp vào nút "Add to Watchlist"
    click_add_to_watchlist(driver)
    
    time.sleep(2)
    #Scroll lên trên 1600px
    driver.execute_script("window.scrollBy(0, -1600);")
    time.sleep(2)
    
    # Mở dropdown và chọn wishlist
    open_dropdown_and_click_watchlist(driver)
    
    # Kiểm tra sản phẩm
    try:
        check_product_title_wl(driver, "Thummanhandiya")
        print("Failed")
    except:
        print("Passed")

#TC05: Bỏ sản phẩm khỏi wl thông qua Buy Now
def test_rm_pro_bn(driver):
    login(driver, "hai6060@gmail.com", "12345")
    #Scroll xuống dưới 1600px
    driver.execute_script("window.scrollBy(0, 1600);")
    time.sleep(2)
    
    #Nút Buy Now
    click_buy_now(driver)
    
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "btn-light").click()
    
    time.sleep(2)
    # Mở dropdown và chọn wishlist
    open_dropdown_and_click_watchlist(driver)
    
    # Kiểm tra sản phẩm
    try:
        check_product_title_wl(driver, "Thummanhandiya")
        print("Failed")
    except:
        print("Passed")