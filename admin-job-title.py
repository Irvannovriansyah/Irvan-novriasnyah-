import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
 
    def test_a_success_login(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        driver.find_element(By.NAME,"username").send_keys("admin") # isi username
        time.sleep(1)
        driver.find_element(By.NAME,"password").send_keys("admin123") # isi password
        time.sleep(1)
        driver.find_element(By.CLASS_NAME,"orangehrm-login-button").click()
        time.sleep(1)

        driver.find_element(By.LINK_TEXT,"Admin").click()
        time.sleep(1)


        # driver.find_element(By.CLASS_NAME,"oxd-dropdown-menu").click() # click add to cart
        # time.sleep(1)

        li_list = driver.find_element(By.XPATH, "//li[@class='oxd-topbar-body-nav-tab --parent']")
        li_list.click()
        time.sleep(3)

        driver.find_element(By.LINK_TEXT,"Job Titles").click()
        time.sleep(3)

        # span_list = driver.find_element(By.CLASS_NAME, "oxd-topbar-body-nav")
        # ul_list = span_list.find_element(By.TAG_NAME,"ul")
        # for item in li_list:
        #     print(item)

        # driver.find_element(By.LINK_TEXT,"Job Titles").click()
        # time.sleep(1)

        

    # def tearDown(self):
    #     self.browser.close()

if __name__ == "__main__":
 unittest.main()
