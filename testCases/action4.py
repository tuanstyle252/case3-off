from selenium.webdriver.support.color import Color
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys

from pageObjects.LoginPage import Loginpage
import time
import datetime
import pytest
from selenium.webdriver.common.by import By
from basetest import BaseTest


class Testaction(BaseTest):

    def test_action4(self):
        lp = Loginpage(self.driver, self.logger)
        lp.login(self.credentials)
        share = self.driver.find_element(By.XPATH, "//*[@id='gfb_app']/main/div/div/div[1]/div[2]/button/i")
        share.click()
        time.sleep(4)
        self.driver.find_element(By.LINK_TEXT, "https://guest-feedback-test.revinate.com/gf/66347/tickets?assigneeIds%5B0%5D=292811&status%5B0%5D=open&ticket_num=&sortBy%5Bid%5D=ts_updated&sortBy%5Bdesc%5D=true").click()
        time.sleep(2)
        self.driver.refresh()
        self.logger.info(f'Passed when validate should refresh page')
        self.driver.close()