import pytest
from selenium.webdriver.common.by import By

from pages.search_flights_results_page import SearchFlightResults
from pages.yatra_launch_page import LaunchPage


@pytest.mark.usefixtures("setUp")
class TestSearchAndVerifyFilter():
    def test_search_flights(self):
        firstPage = LaunchPage(self.driver,self.wait)
        firstPage.departFrom("new delhi")
        firstPage.goingTo("New York")
        firstPage.selectDates("10/04/2024")
        firstPage.searchFlights()

        secondPage = SearchFlightResults(self.driver,self.wait)
        secondPage.setOneStop()

