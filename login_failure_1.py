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

    def test_wrong_username(self):
        """
        Login on the above URL. Enters a wrong username from the list and correct password.
        """
        """
        Examples of wrong usernames are stored in config-failure1.txt. You can choose any of them by changing the index
        for list with : list[1]  or list[2] or list[3]. Also, you can add any other wrong usernames in the txt file.
        """
        #Sleep time is used just for testing, to be able to see what script does

        Dict=yaml.load(open('config-failure1.txt'))
        list=[]
        usernames = Dict['username']
        user_list = usernames.split(", ")
        for user in user_list:
            list.append(user)

        username = self.driver.find_element(By.XPATH, '//input[@type="text"]')
        username.send_keys('{}'.format(list[0]))
        time.sleep(1)

        password = self.driver.find_element(By.XPATH, '//input[@type="password"]')
        password.send_keys('{}'.format(Dict["password"]))
        time.sleep(1)

        login_button = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
        login_button.click()
        time.sleep(3)

        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
                By.XPATH, '//div[contains(text(), "Your username is invalid")]')))
            print('"Your username is invalid" text is displayed on the page')
        except:
            raise Exception(AssertionError)

        self.driver.get_screenshot_as_file('E:\\Python\login_failure1.png')

    def tearDown(self):
        """
        Close the browser.
        """
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
