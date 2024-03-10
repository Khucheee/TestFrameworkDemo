import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.base_driver import BaseDriver


class SearchFlightResults(BaseDriver):
    def __init__(self,driver,wait):
        super().__init__(driver.driver, wait)
        self.driver = driver
        self.wait = wait

    def setOneStop(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH,"//p[@class='font-lightgrey bold'][normalize-space()='1']").click()
        time.sleep(2)
        stopsFromTickets = self.driver.find_elements(By.XPATH,"//span[@class='dotted-borderbtm']")
        self.wait.until(EC.presence_of_all_elements_located)
        for value in stopsFromTickets:
            if value.text=="":
                stopsFromTickets2 = self.driver.find_elements(By.XPATH, "//span[@class='dotted-borderbtm']")
                for value2 in stopsFromTickets2:
                    if value2.text=="":
                        break
                    else:
                        assert value2.text=="1 Stop"
            else:
                assert value.text=="1 Stop"