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
            (By.CLASS_NAME, "orb-nav-section")
        ))


        n=10
        while n > 1:
            print('we are live')
            n-=1
            html = driver.page_source
            page_soup = soup(html,"html.parser")

            li=page_soup.findAll("li",{"class":"gs-u-pb-"})

            matches_list=[]
            for match in range(10):
                col = li[match].findAll("span",{"class":"gs-u-display-none"})
                masaa = li[match].findAll("span", {"class":"sp-c-fixture__status"})
                print(masaa[0].text)
                if masaa[0].text:
                    rem = masaa[0].text
                else:
                    rem = "not started"
                matchDict = { "home": col[0].text, "away": col[1].text,"time":rem }
                matches_list.append(matchDict)

            # print(matches_list)
            time.sleep(3)

    except TimeoutException:
        print("page not loaded")
        driver.quit()
        
if __name__ == "__main__":
    driver = init_driver()
    lookup(driver)
    time.sleep(6)
    driver.quit()