import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class Hover(unittest.TestCase):

    def setUp(self):
        """
        The method instantiates the Chrome WebDriver and navigates to the page given by the URL.
        """
        self.driver = webdriver.Chrome('E:\\Python\chromedriver.exe') #Change with your own path to the driver
        self.driver.get('http://the-internet.herokuapp.com/hovers')
        self.driver.implicitly_wait(20)

    def test_hover(self):
        """
        Hover over each image. When hovering, information about user is displayed.
        """
        # Sleep time is used just for testing, to be able to see what script does

        user1 = self.driver.find_element(By.XPATH, '//div[@class="figure"][1]')
        hover1 = ActionChains(self.driver).move_to_element(user1)
        hover1.perform()
        time.sleep(3)

        # Hovering over image1, it should display info about User1, which can be seen in screenshot_hover1. However,
        # this step can be improved to extract the text that is displayed during hovering over image1.
        self.driver.get_screenshot_as_file('E:\\Python\screenshot_hover1.png')

        user2 = self.driver.find_element(By.XPATH, '//div[@class="figure"][2]')
        hover2 = ActionChains(self.driver).move_to_element(user2)
        hover2.perform()
        time.sleep(3)

        # Hovering over image2, it should display info about User2, which can be seen in screenshot_hover2. However,
        # this step can be improved to extract the text that is displayed during hovering over image2.
        self.driver.get_screenshot_as_file('E:\\Python\screenshot_hover2.png')

        user3 = self.driver.find_element(By.XPATH, '//div[@class="figure"][3]')
        hover3 = ActionChains(self.driver).move_to_element(user3)
        hover3.perform()
        time.sleep(3)

        # Hovering over image3, it should display info about User3, which can be seen in screenshot_hover3. However,
        # this step can be improved to extract the text that is displayed during hovering over image3.
        self.driver.get_screenshot_as_file('E:\\Python\screenshot_hover3.png')

    def tearDown(self):
        """
        Close the browser.
        """
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
