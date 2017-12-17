from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup

my_url='http://www.google.co.ke'

uClient = uReq(my_url)
page_html=uClient.read()
uClient.close()
page_soup = soup(page_html,"html.parser")
page_soup.h1