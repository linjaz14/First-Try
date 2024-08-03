from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import re
import numpy as np
# Then use .find() to display the text following Name: and Favorite Color: 
# (not including any leading spaces or trailing HTML tags that might appear on the same line).

driver = webdriver.Chrome()
driver.get('https://www.studentbostader.se/soker-bostad/lediga-bostader/?omraden=96')

page_source = driver.page_source
driver.quit()

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

myDivs = soup.find_all('div', class_=re.compile('ObjektAddressOmrade'))
myDivs = re.findall("\d+\.\d+",myDivs)
apartmentsOnline = list(map(str,myDivs))

wantedList =    [6.237, 6.223, 6.224, 6.163, 6.164, 6.177,
                8.101, 8.102, 8.103, 8.104, 8.105, 8.106, 8.107, 8.108,
                8.109,8.110 , 8.111, 8.112, 8.113, 8.114, 8.115, 8.116, 8.117, 8.118,
                8.119, 8.120 , 8.121, 8.122, 10.100, 10.101, 10.102, 10.103, 10.104,
                10.105, 10.106, 10.107]

wantedList = list(map(str,wantedList)) # makes list from int to str
print(set(wantedList))
print(apartmentsOnline)
list(set(apartmentsOnline) & set(wantedList))

