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

    def test_action3(self):
        lp = Loginpage(self.driver, self.logger)
        lp.login(self.credentials)
        share = self.driver.find_element(By.XPATH, "//*[@id='gfb_app']/main/div/div/div[1]/div[2]/button/i")
        share.click()

        self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[1]/button").click()
        self.driver.find_element(By.XPATH, "//*[@id='rTest-nav-bar-settings-menu-dropdown']").click()
        self.driver.find_element(By.XPATH, "//*[@id='rTest-nav-bar-settings-user-personal-information']").click()

        # check validate user
        email = self.driver.find_element(By.XPATH, "//*[@id='user_email']").get_attribute("value")

        self.driver.find_element(By.XPATH, "//*[@id='edit_user_form']/div[2]/div/button[2]").click()
        assigned_to = self.driver.find_element(By.XPATH, "//*[@id='assignedTo']/div[1]/div[1]/div[1]/div[1]").text
        from_share_link = f'{assigned_to} <{email}>'
        share = self.driver.find_element(By.XPATH, "//*[@id='gfb_app']/main/div/div/div[1]/div[2]/button/i")
        share.click()
        time.sleep(3)
        check_user_from_share_link = self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/form/div[1]/p").text

        # get element text from
        try:
            assert check_user_from_share_link == from_share_link
            self.logger.info(f'Passed when validate for text '+from_share_link)
        except Exception as ex:
            self.logger.error(f'Failed when validate for text ' + str(ex))

        # get text box
        to_box = self.driver.find_element(By.XPATH, "//*[@id='rtest-to']")
        testInsideTobox = to_box.get_attribute("value")
        # get text subject
        subject_box = self.driver.find_element(By.XPATH, "//*[@id='rtest-subject']")
        testInsidesubject_box = subject_box.get_attribute("value")
        # get text note
        note_box = self.driver.find_element(By.XPATH, "//*[@id='rtest-note']")
        testInsideNotebox = note_box.get_attribute("value")

        # check verify
        try:
            assert testInsideTobox == ""
            self.logger.info(f'Passed when validate for to the textbox(no data by de fault)')
        except Exception as ex:
            self.logger.error(f'Failed when validate for to the textbox(no data by de fault) '+str(ex))

        try:
            assert testInsidesubject_box == ""
            self.logger.info(f'Passed when validate for to the subject:(no data by de fault)')
        except Exception as ex:
            self.logger.error(f'Failed when validate for to the subject:(no data by de fault) ' + str(ex))

        try:
            assert testInsideNotebox == ""
            self.logger.info(f'Passed when validate for your note:the textbox:(no data by the default)')
        except Exception as ex:
            self.logger.error(f'Failed when validate for your note:the textbox:(no data by the default) ' + str(ex))

        msg = self.driver.find_element(By.XPATH, "//*[@id='gfb-cc']").is_selected()
        try:
            assert msg == False
            self.logger.info(f'Passed when validate for the copy myself:checkbox(unselect by default)')
        except Exception as ex:
            self.logger.error(f'Failed when validate for the copy myself:checkbox(unselect by default) ' + str(ex))

        link = self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/form/div[6]/p/a").is_displayed()
        try:
            assert link == True
            self.logger.info(f'Passed when validate for the link current link of the "tickets"page')
        except Exception as ex:
            self.logger.error(f'Failed when validate for the link current link of the "tickets"page ' + str(ex))

        link_priva = self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[3]/a").is_displayed()
        try:
            assert link_priva == True
            self.logger.info(f'Passed when validate for the"privacy policy"link')
        except Exception as ex:
            self.logger.error(f'Failed when validate for the"privacy policy"link ' + str(ex))

        send_submit = self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[3]/button")
        try:
            assert send_submit.is_displayed() == True
            self.logger.info(f'Passed when validate for text SEND button')
        except Exception as ex:
            self.logger.error(f'Failed when validate for text SEND button ' + str(ex))

        x_cancal = self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[1]/button")
        try:
            assert x_cancal.is_displayed() == True
            self.logger.info(f'Passed when validate for text X button')
        except Exception as ex:
            self.logger.error(f'Failed when validate for text X button ' + str(ex))

