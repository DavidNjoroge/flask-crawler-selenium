from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time
# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
# import beautifulsoup4 as BeautifulSoup
# from bs4 import BeautifulSoup

def init_driver():
    # driver = webdriver.Firefox()
    driver = webdriver.Chrome('chromedriver')
    
    driver.wait = WebDriverWait(driver, 5)
    return driver
 
 
def lookup(driver):
    driver.get("http://127.0.0.1:3002/")
    try:
        home=driver.wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "team")
        
        ))
        # soup=BeautifulSoup(driver.page_source)
        # soup= BeautifulSoup(driver.page_source, "html.parser")

        # print('<><><><><>><>hurray<><><><><><>')
        # print(soup.find_all("div",class_='content'))
        # print(soup.find_all("div", data_type="container"))
        # for div in soup.find_all(class_='content'):
        #     print link.get('href',None),link.get_text()
    except TimeoutException:
        print("page not loaded")
if __name__ == "__main__":
    driver = init_driver()
    lookup(driver)
    time.sleep(5)
    driver.quit()