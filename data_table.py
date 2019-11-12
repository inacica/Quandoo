import unittest
import time
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup


class Login(unittest.TestCase):

    def setUp(self):
        """
        The method instantiates the Chrome WebDriver and navigates to the page given by the URL.
        """
        self.driver = webdriver.Chrome('E:\\Python\chromedriver.exe') #Change with your own path to the driver
        self.driver.get('http://the-internet.herokuapp.com/tables')
        self.driver.implicitly_wait(10)

    def test_sort_ascending(self):
        """
        Lists alphabetically all the members according to the last name
        """
        # Sleep time is used just for testing, to be able to see what script does

        last_names_list = []
        html = urllib.request.urlopen('http://the-internet.herokuapp.com/tables').read()
        soup = BeautifulSoup(html, "html5lib")
        table = soup.find("table", attrs={"id":"table2"})
        table_tr = table.find("tbody").findAll("tr")

        td_0 = table_tr[0].find("td")
        last_name_0 = td_0.text
        last_names_list.append(last_name_0)

        td_1 = table_tr[1].find("td")
        last_name_1 = td_1.text
        last_names_list.append(last_name_1)

        td_2 = table_tr[2].find("td")
        last_name_2 = td_2.text
        last_names_list.append(last_name_2)

        td_3 = table_tr[3].find("td")
        last_name_3 = td_3.text
        last_names_list.append(last_name_3)

        ascendent_last_names_list = sorted(last_names_list)

    #Here, the if statement could be improved with a while loop, but i had some issues with iterating in html.

        if last_name_0 != ascendent_last_names_list[0]:
            last_name = self.driver.find_element(By.XPATH, '//span[@class="last-name"]/parent::th')
            last_name_t = ActionChains(self.driver).move_to_element(last_name)
            time.sleep(5)
            last_name_t.click().perform()
            time.sleep(5)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            self.driver.get_screenshot_as_file('E:\\Python\screenshot_ascending.png')

    def test_sort_desscending(self):
        """
        Lists alphabetically all the members according to the last name
        """
        # Sleep time is used just for testing, to be able to see what script does

        last_names_list = []
        html = urllib.request.urlopen('http://the-internet.herokuapp.com/tables').read()
        soup = BeautifulSoup(html, "html5lib")
        table = soup.find("table", attrs={"id":"table2"})
        table_tr = table.find("tbody").findAll("tr")

        td_0 = table_tr[0].find("td")
        last_name_0 = td_0.text
        last_names_list.append(last_name_0)

        td_1 = table_tr[1].find("td")
        last_name_1 = td_1.text
        last_names_list.append(last_name_1)

        td_2 = table_tr[2].find("td")
        last_name_2 = td_2.text
        last_names_list.append(last_name_2)

        td_3 = table_tr[3].find("td")
        last_name_3 = td_3.text
        last_names_list.append(last_name_3)

        descendent_last_names_list = sorted(last_names_list, reverse=True)
        print(descendent_last_names_list)

        # The same as above. The if statement could be improved.
        if (last_name_0 != descendent_last_names_list[0]) or (last_name_1 != descendent_last_names_list[1]):
            last_name = self.driver.find_element(By.XPATH, '//span[@class="last-name"]/parent::th')
            last_name_t = ActionChains(self.driver).move_to_element(last_name)
            time.sleep(3)
            last_name_t.click().perform()
            time.sleep(3)
            last_name_t = ActionChains(self.driver).move_to_element(last_name)
            time.sleep(3)
            last_name_t.click().perform()
            time.sleep(3)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            self.driver.get_screenshot_as_file('E:\\Python\screenshot_desscending.png')

    def tearDown(self):
        """
        Close the browser.
        """
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
