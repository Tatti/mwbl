from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

password="admin" #admin is the default password, change if needed.
address="http://tplinkmifi.net/login.html" # Can also use IP of the device

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)
driver.get(address)
time.sleep(1)
elem = driver.find_element_by_id("password")
elem.send_keys(password)
elem.send_keys(Keys.ENTER)
assert "No results found." not in driver.page_source

time.sleep(3)
html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
soup = BeautifulSoup(html, 'html.parser')

for ultag in soup.find_all('ul', {'id': 'top_icon_layout'}):
    for litag in ultag.find_all('li'):
        att = litag.a.i
        if att is not None:
            if att.get('id') == 'topElectricity':
                bat = litag.attrs
                print(bat.get("title"))

driver.close()
