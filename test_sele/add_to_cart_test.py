import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from navigation import login
from navigation import click_add_to_cart
from navigation import check_product_title_cart
from wishlist_test import test_wl_pro
from navigation import click_buy_now
from navigation import accept_alert_and_go_to_cart
from navigation import select_educational_category
from navigation import click_add_to_watchlist_out
from navigation import check_product_title_wl
from navigation import open_dropdown_and_click_watchlist

# Fixture to initialize and close the browser driver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
    
#TC01: Trường hợp thêm sản phẩm cách thông thường
def test_add_fanpage(driver):
    login(driver, "hai6060@gmail.com", "12345")
    
    #Scroll xuống dưới 1600px
    driver.execute_script("window.scrollBy(0, 1600);")
    time.sleep(2)
    
     # Nhấp vào nút thêm vào giỏ hàng
    click_add_to_cart(driver)
    
    time.sleep(2)
    #Scroll lên trên 1600px
    driver.execute_script("window.scrollBy(0, -1600);")
    time.sleep(2)
    
    cart_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='col-1 col-lg-2 ms-5 ms-lg-0 cart-icon btn btn-info' and @onclick=\"window.location='cart.php'\"]"))
    )
    cart_icon.click()
    check_product_title_cart(driver, "Thummanhandiya")
    time.sleep(2)
    
#TC02: Thêm sản phẩm bằng Wishlist
def test_add_wl(driver):
    test_wl_pro(driver)
    
    #Nhấn vào nút thêm vào giỏ hàng
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-warning mb-2' and @onclick='addToCart(18);']"))
    )
    add_to_cart_button.click()
    
    #Chấp nhận thông báo và vào giỏ hàng
    accept_alert_and_go_to_cart(driver)
    time.sleep(2)
    
    # Kiểm tra sản phẩm trong giỏ hàng
    check_product_title_cart(driver, "Thummanhandiya")


#TC03: Thêm sản phẩm bằng Buy Now
def test_add_bn(driver):
    login(driver, "hai6060@gmail.com", "12345")
    #Scroll xuống dưới 1600px
    driver.execute_script("window.scrollBy(0, 1600);")
    time.sleep(2)
    
    #Nút Buy Now
    click_buy_now(driver)
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "btn-warning").click()
        
    #Chấp nhận thông báo và vào giỏ hàng
    accept_alert_and_go_to_cart(driver)
    time.sleep(2)
    
    # Kiểm tra sản phẩm trong giỏ hàng
    check_product_title_cart(driver, "Thummanhandiya")

#TC04: Bỏ sản phẩm khỏi giỏ hàng
def test_rm_pro(driver):
    test_add_fanpage(driver)
    time.sleep(3)
    driver.find_element(By.CLASS_NAME, "btn-danger").click()
    
    # Tự động nhấn phím ENTER để xác nhận thông báo
    WebDriverWait(driver, 10).until(
        EC.alert_is_present()
    )
    alert = driver.switch_to.alert
    alert.accept()

    # Kiểm tra thông báo "You have no items in your Cart yet."
    empty_cart_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//label[@class='form-label fs-1 fw-bold' and contains(text(), 'You have no items in your Cart yet.')]"))
    )
    assert empty_cart_message.is_displayed(), "Empty cart message not displayed"


#TC05: Thêm sản phẩm đã hết hàng vào giỏ hàng (Failed)
def test_add_out_of_stock(driver):
    login(driver, "hai6060@gmail.com", "12345")
    
    #Chọn thể loại Educational
    select_educational_category(driver)
    
    #Thêm sản phẩm vào wl
    click_add_to_watchlist_out(driver)
    
    time.sleep(2)
    # Mở dropdown và chọn wishlist
    open_dropdown_and_click_watchlist(driver)
    
    #Kiểm tra sản phẩm
    check_product_title_wl(driver, "Physics Paper Rewiew 2020")
    
    #Thêm vào giỏ hàng
    driver.find_element(By.CLASS_NAME, "btn-warnin").click()
    
    #Chấp nhận thông báo và vào giỏ hàng
    accept_alert_and_go_to_cart(driver)
    time.sleep(2)
    
    assert not check_product_title_cart(driver, "Physics Paper Rewiew 2020"), "Failed: Product is in the cart"
    
