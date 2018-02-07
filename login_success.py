import unittest
import yaml
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login(unittest.TestCase):

    def setUp(self):
        """
        The method instantiates the Chrome WebDriver and navigates to the page given by the URL.
        """
        self.driver = webdriver.Chrome('E:\\Python\chromedriver.exe')
        self.driver.get('http://the-internet.herokuapp.com/login')
        self.driver.implicitly_wait(20)

    def test_login_successful(self):
        """
        Login on the above URL. Enters the correct username and password.
        """
        # Sleep time is used just for testing, to be able to see what script does

        Dict=yaml.load(open('config.txt'))

        username = self.driver.find_element(By.XPATH, '//input[@type="text"]')
        username.send_keys('{}'.format(Dict["username"]))
        time.sleep(1)

        password = self.driver.find_element(By.XPATH, '//input[@type="password"]')
        password.send_keys('{}'.format(Dict["password"]))
        time.sleep(1)

        login_button = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
        login_button.click()
        time.sleep(3)

        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
                By.XPATH, '//div[contains(text(), "You logged into a secure area!")]')))
            print('"You logged into a secure area!" text is displayed on the page')
        except:
            raise Exception(AssertionError)

        self.driver.get_screenshot_as_file('E:\\Python\login_success.png')

    def tearDown(self):
        """
        Close the browser.
        """
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
