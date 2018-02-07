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
        self.driver = webdriver.Chrome('E:\\Python\chromedriver.exe') #Change with your own path to the driver
        self.driver.get('http://the-internet.herokuapp.com/login')
        self.driver.implicitly_wait(20)

    def test_wrong_password(self):
        """
        Login on the above URL. Enters a correct username and a wrong password from the list.
        """
        """
        Examples of wrong passwords are stored in config-failure2.txt. You can choose any of them by changing the index
        for list with : list[1]  or list[2] or list[3]. Also, you can add any other wrong passwords in the txt file.
        """
        #Sleep time is used just for testing, to be able to see what script does

        Dict=yaml.load(open('config-failure2.txt'))
        list=[]
        passwords = Dict['password']
        passw_list = passwords.split(", ")
        for password in passw_list:
            list.append(password)

        username = self.driver.find_element(By.XPATH, '//input[@type="text"]')
        username.send_keys('{}'.format(Dict["username"]))
        time.sleep(1)

        password = self.driver.find_element(By.XPATH, '//input[@type="password"]')
        password.send_keys('{}'.format(list[0]))
        time.sleep(1)

        login_button = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
        login_button.click()
        time.sleep(3)

        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
                By.XPATH, '//div[contains(text(), "Your password is invalid!")]')))
            print('"Your password is invalid" text is displayed on the page')
        except:
            raise Exception(AssertionError)

        self.driver.get_screenshot_as_file('E:\\Python\login_failure2.png')

    def tearDown(self):
        """
        Close the browser.
        """
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
