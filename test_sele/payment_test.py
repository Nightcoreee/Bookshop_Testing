import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from navigation import login
from navigation import click_buy_now

# Fixture to initialize and close the browser driver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_payment_bn(driver):
    login(driver, "hai6060@gmail.com", "12345")
    #Scroll xuống dưới 1600px
    driver.execute_script("window.scrollBy(0, 1600);")
    time.sleep(2)
    
    #Nút Buy Now
    click_buy_now(driver)
    
    driver.find_element(By.ID, "payhere-payment").click()
    time.sleep(4)
    
     # Chờ cho đến khi trang thanh toán thành công tải xong
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Payment Success')]"))
    )
    
    # Kiểm tra thông báo thành công
    success_message = driver.find_element(By.XPATH, "//h1[contains(text(), 'Payment Success')]")
    assert success_message.is_displayed(), "Payment was not successful"
    