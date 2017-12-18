#!usr/bin/env python3.6

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url='http://www.bbc.co.uk/sport/football/scores-fixtures'

uClient = uReq(my_url)
page_html=uClient.read()
uClient.close()
page_soup = soup(page_html,"html.parser")

li=page_soup.findAll("li",{"class":"gs-u-pb-"})

matches_list=[]
for match in li:
     col=match.findAll("span",{"class":"gs-u-display-none"})
     matchDict={"home":col[0].text,"away":col[1].text}
     matches_list.append(matchDict)

print(matches_list)