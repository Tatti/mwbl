from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import sys

password="admin" #admin is the default password, change if needed.
address="http://tplinkmifi.net/login.html" # Can also use IP of the device

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)

driver.get(address)

try:
    elem = wait.until(EC.visibility_of_element_located((By.ID, 'password')))
except:
    print("ERR")
    driver.quit()
    sys.exit()

elem.send_keys(password)
elem.send_keys(Keys.ENTER)

batteryLevelFound = False
while batteryLevelFound == False:
    html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    soup = BeautifulSoup(html, 'html.parser')
    for ultag in soup.find_all('ul', {'id': 'top_icon_layout'}):
        for litag in ultag.find_all('li'):
            att = litag.a.i
            if att is not None:
                if att.get('id') == 'topElectricity':
                    bat = litag.attrs
                    if bat.get("title"):
                        print(bat.get("title"))
                        batteryLevelFound = True

driver.quit()
