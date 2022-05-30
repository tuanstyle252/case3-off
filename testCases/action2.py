from selenium.webdriver.support.color import Color
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys

from pageObjects.LoginPage import Loginpage
import time

from selenium.webdriver.common.by import By
from basetest import BaseTest


class Testaction2(BaseTest):

    def test_action2(self):
        lp = Loginpage(self.driver, self.logger)
        lp.login(self.credentials)
        share = self.driver.find_element(By.XPATH, "//*[@id='gfb_app']/main/div/div/div[1]/div[2]/button/i")
        try:
            if (share.is_displayed()):
                share.click()
                self.logger.info(f'Passed when validate the"Share This Page" modal should be shown')
            else:
                self.logger.error(f'Failed when validate the"Share This Page" modal should be shown')
        except:
            pass




