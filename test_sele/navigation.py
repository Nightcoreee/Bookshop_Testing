import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

#trang đăng nhập
def go_to_sign_in_page(driver):
    driver.get("http://localhost/PHP_E_Commerce_Web_Application_MySQL/bookshop/signIn.php")

#trang đăng ký
def go_to_sign_up_page(driver):
    driver.get("http://localhost/PHP_E_Commerce_Web_Application_MySQL/bookshop/signUp.php")

#trang chủ khi đăng nhập
def go_to_home_page(driver):
    driver.get("http://localhost/PHP_E_Commerce_Web_Application_MySQL/bookshop/home.php")

#Check sản phẩm ở search
def check_product_title(driver, expected_title):
    try:
        # Chờ cho đến khi sản phẩm xuất hiện trên trang kết quả
        product_title = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h5.card-title.fw-bold.fs-6"))
        )
        
        # In ra giá trị thực tế của tiêu đề sản phẩm
        print("Actual product title:", product_title.text)
        
        # Kiểm tra nội dung của tiêu đề sản phẩm
        assert product_title.text.strip() == expected_title
    except Exception as e:
        print(f"Error: {e}")
        raise

#Check sản phẩm trong wishlist
def check_product_title_wl(driver, expected_title):
    try:
        # Chờ cho đến khi sản phẩm xuất hiện trên trang kết quả
        product_title = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h5.card-title.fs-2.fw-bold.text-light"))
        )
        
        # In ra giá trị thực tế của tiêu đề sản phẩm
        print("Actual product title:", product_title.text)
        
        # Kiểm tra nội dung của tiêu đề sản phẩm
        assert product_title.text.strip() == expected_title
    except Exception as e:
        print(f"Error: {e}")
        raise
    
#Check sản phẩm trong giỏ hàng
def check_product_title_cart(driver, expected_title):
    try:
        # Chờ cho đến khi sản phẩm xuất hiện trên trang kết quả
        product_title = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h3.card-title"))
        )
        
        # In ra giá trị thực tế của tiêu đề sản phẩm
        print("Actual product title:", product_title.text)
        
        # Kiểm tra nội dung của tiêu đề sản phẩm
        assert product_title.text.strip() == expected_title
    except Exception as e:
        print(f"Error: {e}")
        raise

#Tự động đăng nhập
def login(driver, email, password):
    driver.get("http://localhost/PHP_E_Commerce_Web_Application_MySQL/bookshop/signIn.php")
    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    
    WebDriverWait(driver, 10).until(EC.url_to_be("http://localhost/PHP_E_Commerce_Web_Application_MySQL/bookshop/home.php"))
    assert driver.current_url == "http://localhost/PHP_E_Commerce_Web_Application_MySQL/bookshop/home.php"

#Mở menu ở trang chủ
def open_dropdown_and_click_watchlist(driver):
    # Nhấp vào nút dropdown
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "dropdown-toggle"))
    ).click()
    
    # Nhấp vào thẻ Watchlist
    watchlist_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='dropdown-item' and @href='watchlist.php']"))
    )
    watchlist_button.click()

#Nút Buy Now
def click_buy_now(driver):
    buy_now_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='singleProductView.php?id=18' and @class='col-12 btn btn-dark']"))
    )
    buy_now_button.click()

#Nút Add to Watchlist
def click_add_to_watchlist(driver):
    add_to_watchlist_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='col-5 btn btn-success mt-2 border border-primary' and @onclick='addToWatchlist(18);']"))
    )
    add_to_watchlist_button.click()

#Tự động nhập email và password
def autofill_login(driver, email, password):
    driver.get("http://localhost/PHP_E_Commerce_Web_Application_MySQL/bookshop/signIn.php")
    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "password").send_keys(password)


def click_forgot_password(driver):
    driver.find_element(By.LINK_TEXT, "Forget Password?").click()
    
    # Tự động nhấn phím ENTER hoặc SPACE để xác nhận thông báo
    WebDriverWait(driver, 10).until(
        EC.alert_is_present()
    )
    alert = driver.switch_to.alert
    alert.accept()

#Tự click thêm vào giỏ hàng
def click_add_to_cart(driver):
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//i[@class='bi bi-cart-plus-fill text-white fs-5' and @onclick='addToCart(18);']"))
    )
    add_to_cart_button.click()
    
    WebDriverWait(driver, 10).until(
        EC.alert_is_present()
    )
    alert = driver.switch_to.alert
    alert.accept()

#Chấp nhận thông báo và vào giỏ hàng
def accept_alert_and_go_to_cart(driver):
    # Chấp nhận thông báo từ localhost
    WebDriverWait(driver, 10).until(
        EC.alert_is_present()
    )
    alert = driver.switch_to.alert
    alert.accept()
    
    # Vào giỏ hàng
    cart_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='col-1 col-lg-2 ms-5 ms-lg-0 cart-icon btn btn-info' and @onclick=\"window.location='cart.php'\"]"))
    )
    cart_icon.click()


def select_educational_category(driver):
    # Chờ cho đến khi thẻ <select> có thể nhấp được
    category_select = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "catogory"))
    )
    
    # Tạo đối tượng Select và chọn mục "Educational"
    select = Select(category_select)
    select.select_by_visible_text("Educational")

def click_add_to_watchlist_out(driver):
    add_to_watchlist_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='col-5 btn btn-success mt-2 border border-primary' and @onclick='addToWatchlist(9);']"))
    )
    add_to_watchlist_button.click()


def login_2(driver, email, password):
    driver.get("http://localhost/PHP_E_Commerce_Web_Application_MySQL/bookshop/signIn.php")
    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    
    WebDriverWait(driver, 10).until(EC.url_to_be("http://localhost/PHP_E_Commerce_Web_Application_MySQL/bookshop/home.php"))
    assert driver.current_url == "http://localhost/PHP_E_Commerce_Web_Application_MySQL/bookshop/home.php"


#Nút Reset Password
def click_reset_button_and_accept_alert(driver):
    try:
        reset_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary' and @onclick='resetPassword();']"))
        )
        reset_button.click()
    except Exception as e:
        print(f"Error clicking reset button: {e}")
        # Sử dụng JavaScript để nhấp vào nút nếu cần thiết
        driver.execute_script("arguments[0].click();", reset_button)
        
    WebDriverWait(driver, 10).until(
        EC.alert_is_present()
    )
    alert = driver.switch_to.alert
    alert.accept()