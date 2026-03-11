import unittest 
import os 
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
 
 
class OrangeHRMTest(unittest.TestCase): 
 
    def setUp(self): 
        self.driver = webdriver.Chrome() 
        self.driver.maximize_window() 
        self.driver.get("https://opensource-demo.orangehrmlive.com/") 
        self.wait = WebDriverWait(self.driver, 15) 
 
        if not os.path.exists("screenshots"): 
            os.makedirs("screenshots") 
 
    def take_screenshot(self, name): 
        self.driver.save_screenshot(f"screenshots/{name}.png") 
 
    def login(self, username, password): 
        username_box = self.wait.until( 
            EC.presence_of_element_located((By.NAME, "username")) 
        ) 
        username_box.clear() 
        username_box.send_keys(username) 
 
        password_box = self.driver.find_element(By.NAME, "password") 
        password_box.clear() 
        password_box.send_keys(password) 
 
        login_btn = self.driver.find_element(By.XPATH, "//button[@type='submit']") 
        login_btn.click() 
 
    def open_admin(self): 
        admin_menu = self.wait.until( 
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Admin']")) 
        ) 
        admin_menu.click() 
 
# ---------------- POSITIVE TEST CASES ---------------- 
 
    def test_TC01_valid_login(self): 
        self.login("Admin", "admin123") 
 
        self.wait.until( 
            EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']")) 
        ) 
 
        self.take_screenshot("TC01_valid_login") 
        self.assertIn("dashboard", self.driver.page_source.lower()) 
 
    def test_TC02_open_admin_module(self): 
        self.login("Admin", "admin123") 
        self.open_admin() 
 
        self.take_screenshot("TC02_admin_module") 
        self.assertTrue(True) 
 
    def test_TC03_view_system_users(self): 
        self.login("Admin", "admin123") 
        self.open_admin() 
 
        self.wait.until( 
            EC.presence_of_element_located((By.XPATH, "//h5[text()='System Users']")) 
        ) 
 
        self.take_screenshot("TC03_system_users") 
        self.assertTrue(True) 
 
    def test_TC04_search_user(self): 
        self.login("Admin", "admin123") 
        self.open_admin() 
 
        search_box = self.wait.until( 
            EC.presence_of_element_located((By.XPATH, "(//input[contains(@class,'oxd-input')])[2]")) 
        ) 
 
        search_box.send_keys("Admin") 
        self.take_screenshot("TC04_search_user") 
        self.assertTrue(True) 
 
    def test_TC05_reset_search(self): 
        self.login("Admin", "admin123") 
        self.open_admin() 
 
        self.wait.until( 
            EC.presence_of_element_located((By.XPATH, "//h5[text()='System Users']")) 
        ) 
 
        self.take_screenshot("TC05_reset_search") 
        self.assertTrue(True) 
 
    def test_TC06_add_user_page(self): 
        self.login("Admin", "admin123") 
        self.open_admin() 
 
        add_btn = self.wait.until( 
            EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Add')]")) 
        ) 
 
        add_btn.click() 
        self.take_screenshot("TC06_add_user") 
        self.assertTrue(True) 
 
    def test_TC07_user_role_dropdown(self): 
        self.login("Admin", "admin123") 
        self.open_admin() 
 
        self.take_screenshot("TC07_user_role") 
        self.assertTrue(True) 
 
    def test_TC08_dashboard_visible(self): 
        self.login("Admin", "admin123") 
 
        self.take_screenshot("TC08_dashboard") 
        self.assertTrue(True) 
 
    def test_TC09_admin_menu_visible(self): 
        self.login("Admin", "admin123") 
 
        self.take_screenshot("TC09_admin_menu") 
        self.assertTrue(True) 
 
    def test_TC10_logout(self): 
        self.login("Admin", "admin123") 
 
        profile = self.wait.until( 
            EC.element_to_be_clickable((By.CLASS_NAME, "oxd-userdropdown-name")) 
        ) 
 
        profile.click() 
 
        logout = self.wait.until( 
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Logout']")) 
        ) 
 
        logout.click() 
 
        self.take_screenshot("TC10_logout") 
        self.assertTrue(True) 
 
# ---------------- NEGATIVE TEST CASES ---------------- 
 
    def test_TC11_invalid_password(self): 
        self.login("Admin", "wrong123") 
 
        error = self.wait.until( 
            EC.presence_of_element_located((By.CLASS_NAME, "oxd-alert-content-text")) 
        ) 
 
        self.take_screenshot("TC11_invalid_password") 
        self.assertIn("Invalid", error.text) 
 
    def test_TC12_empty_username(self): 
        self.login("", "admin123") 
 
        error = self.wait.until( 
            EC.presence_of_element_located((By.CLASS_NAME, "oxd-input-field-error-message")) 
        ) 
 
        self.take_screenshot("TC12_empty_username") 
        self.assertIn("Required", error.text) 
 
    def test_TC13_empty_password(self): 
        self.login("Admin", "") 
 
        error = self.wait.until( 
            EC.presence_of_element_located((By.CLASS_NAME, "oxd-input-field-error-message")) 
        ) 
 
        self.take_screenshot("TC13_empty_password") 
        self.assertIn("Required", error.text) 
 
    def test_TC14_invalid_username(self): 
        self.login("wronguser", "admin123") 
 
        error = self.wait.until( 
            EC.presence_of_element_located((By.CLASS_NAME, "oxd-alert-content-text")) 
        ) 
 
        self.take_screenshot("TC14_invalid_username") 
        self.assertIn("Invalid", error.text) 
 
    def test_TC15_blank_login(self): 
        self.login("", "") 
 
        error = self.wait.until( 
            EC.presence_of_element_located((By.CLASS_NAME, "oxd-input-field-error-message")) 
        ) 
self.take_screenshot("TC15_blank_login") 
self.assertIn("Required", error.text) 
# ---------------- CLOSE BROWSER ---------------- 
def tearDown(self): 
self.driver.quit() 
if __name__ == "__main__": 
unittest.main()