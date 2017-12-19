#!usr/bin/env python3.6

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



def init_driver():
    driver = webdriver.Chrome('chromedriver')
    
    driver.wait = WebDriverWait(driver, 5)
    return driver
 
def lookup(driver):
    driver.get("http://www.bbc.co.uk/sport/football/scores-fixtures")
    try:
        home=driver.wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "gs-u-vh")
        ))
        page_soup = soup(home,"html.parser")

        li=page_soup.findAll("li",{"class":"gs-u-pb-"})

        matches_list=[]
        for match in li:
            col=match.findAll("span",{"class":"gs-u-display-none"})
            matchDict={"home":col[0].text,"away":col[1].text}
            matches_list.append(matchDict)

        print(matches_list)

    except TimeoutException:
        print("page not loaded")
if __name__ == "__main__":
    driver = init_driver()
    lookup(driver)
    time.sleep(5)
    driver.quit()