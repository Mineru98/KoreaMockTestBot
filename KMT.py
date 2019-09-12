import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import time
from datetime import datetime

# time setting
now = datetime.now()

# chrome setting
_chrome_options = webdriver.ChromeOptions() 
_chrome_options.add_argument('disable-infobars')
driver = webdriver.Chrome('C:\chromedriver.exe',options=_chrome_options)

# searching bot
def search_start(year=(now.year),month=(now.month),_class=3):
    url = 'http://www.ebsi.co.kr/ebs/ent/entd/retrieveTrlNaatLiveGrdCutlnNw2017.ebs?examCd=%dN%02d&type=FULL_SUB&stdntGrd=%d' % (year+1,month,_class)
    driver.get(url)
    count = 1
    while True:
        try:
            path = '/html/body/div/div/div[3]/div[1]/ul/li[%d]/a' % count
            count = count + 1
            print(path)
            driver.find_element_by_xpath(path).click()
            element = WebDriverWait(driver,3).until(EC.presence_of_element_located((By.XPATH,'//*[@id="titles"]/th[2]')))
            time.sleep(0.01)
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            step1 = soup.html.tbody.tr
            result = step1.find('td',{'class':''})
            for i in range(1,9):
                try:
                    print("%d 등급" % i)
                    while True:
                        try:
                            result = result.next_sibling
                            if result is not None:
                                print(result.text + ',')
                        except AttributeError:
                             break
                    step1 = step1.next_sibling
                    result = step1.find('td',{'class':''})
                except AttributeError:
                    break
        except NoSuchElementException:
            break

search_start(2018,10,3)
