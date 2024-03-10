import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class LaunchPage(BaseDriver):
    def __init__(self,driver,wait):
        super().__init__(driver,wait)
        self.driver = driver
        self.wait = wait

    def departFrom(self,location):
        departFrom = self.driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']")
        departFrom.click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH,"(//p[@class='ac_cityname'])[1]")))
        departFrom.send_keys(Keys.ENTER)

    def goingTo(self,location):
        print("going to function started")
        self.wait.until(EC.invisibility_of_element((By.XPATH,"(//p[normalize-space()='BOM'])[1]")))
        goingto = self.driver.find_element(By.XPATH,"(//input[@id='BE_flight_arrival_city'])[1]")
        goingto.send_keys(location)
        self.wait.until(EC.element_to_be_clickable((By.XPATH,"(//li[@class='active ac_over'])[1]")))
        goingto.send_keys(Keys.ENTER)

    def selectDates(self,date):
        self.driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_date']").click()
        while True:
            dates = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//tr"))).find_elements(By.XPATH,"//table[@class!='days-head']//descendant::td[@class!='inActiveTD weekend']")
            if dates[0].get_attribute("data-date")!=None:
                break
            print("пока нет даты")

        for element in dates:
            if element.get_attribute("data-date")==date:
                self.wait.until(EC.element_to_be_clickable((By.XPATH,"//td[@data-date='10/04/2024']")))
                element.click()
                break

    def searchFlights(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@value="Search Flights"]'))).click()

