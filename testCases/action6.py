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

    def test_action6(self):
        lp = Loginpage(self.driver, self.logger)
        lp.login(self.credentials)

        share = self.driver.find_element(By.XPATH, "//*[@id='gfb_app']/main/div/div/div[1]/div[2]/button/i")
        share.click()
        #get element field input
        self.driver.find_element(By.XPATH, "//*[@id='rtest-to']").clear()
        self.driver.find_element(By.XPATH, "//*[@id='rtest-to']").send_keys("phananhtuan792@gmail.con")
        time.sleep(3)
        # get element field subject
        self.driver.find_element(By.XPATH, "//*[@id='rtest-subject']").send_keys("automation")

        # get element field your note
        self.driver.find_element(By.XPATH, "//*[@id='rtest-note']").send_keys("automation")

        #get element field send
        self.driver.find_element(By.XPATH, "//*[@class='btn btn-primary']").click()

        expectedMessage = "Success! This page has been shared."
        # get text alert noti
        message_success = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='rtest-alert-notifications']/div[1]")))
        act_message_success = message_success.text

        # check color
        message_success = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='rtest-alert-notifications']/div[1]"))).value_of_css_property("background-color")
        hex = Color.from_string(message_success).hex
        try:
            assert hex == "#99dfa1"
            self.logger.info(f'Passed when validate color green for the message')
        except Exception as ex:
            self.logger.error(f'Failed when validate color green for the message '+str(ex))
        #check verify noti
        try:
            assert act_message_success == expectedMessage
            self.logger.info(f'Passed when validate for text message "succes!this page has been shared')
        except Exception as ex:
            self.logger.error(f'Passed when validate for text message "succes!this page has been shared '+str(ex))


