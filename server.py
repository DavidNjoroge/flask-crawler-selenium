#!/usr/bin/env python3.6

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from crawlers import all_games,check_games

def init_driver():
    driver = webdriver.Chrome('chromedriver')
    
    driver.wait = WebDriverWait(driver, 5)
    return driver
 
def lookup(driver):
    driver.get("http://www.bbc.co.uk/sport/football/scores-fixtures")
    try:
        home=driver.wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "orb-nav-section")
        ))
        status=True
        
        html = driver.page_source
        page_soup = soup(html,"html.parser")
        all_games_dict = all_games(page_soup)
        return all_games_dict
        # for i in range(6):
        # while status:
        #     time.sleep(60)
        #     html = driver.page_source
        #     page_soup = soup(html,"html.parser")
        #     status,games=check_games(all_games_dict,page_soup)
        #     print(status,len(games))
        # print(all_games_dict)

    except Exception:
        print("shit happened",Exception)
        driver.quit()
        
# if __name__ == "__main__":
#     driver = init_driver()
#     lookup(driver)
#     # time.sleep(6)
#     driver.quit()

def request():
    driver = init_driver()
    returned = lookup(driver)
    driver.quit()
    return returned