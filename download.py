from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import csv
import sys
from bs4 import BeautifulSoup
from lxml import html



fire_path=r"/home/bhuppi/Documents/agri_data/chromedriver"
driver=webdriver.Chrome(fire_path)
wait = WebDriverWait(driver,20)
source='https://www.latlong.net'
r = driver.get(source)
#xpath = "//*[@id=\"place\"]"
#xpath = "//*[@id=\"ctl00_MainContent_Rbl_Rpt_type\"]/tbody/tr[1]/td/label"
#id_ = "//*[@id=\"ctl00_MainContent_Rbl_Rpt_type_1\"]"
#id_ = "ctl00_MainContent_Rbl_Rpt_type_1"
#elements = driver.find_element_by_id(id_)
#elements.click()
#
xpath = "//*[@id=\"place\"]"
elements = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
elements.click()
#
#start_date=sys.argv[1]
#end_date=sys.argv[2]
#xpath = "//*[@id=\"ctl00_MainContent_Txt_FrmDate\"]"
#elements = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
#elements.click()
#elements.send_keys(start_date)
#
#driver.find_element_by_xpath("//body").click()
#xpath = "//*[@id=\"ctl00_MainContent_Txt_ToDate\"]"
#elements = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
#elements.click()
#elements.send_keys(end_date)
#driver.find_element_by_xpath("//body").click()
#var = int(sys.argv[3])
#for i in range(var, var+1):
#    xpath ="//*[@id=\"ctl00_MainContent_Lst_Commodity\"]/option["+str(i)+"]"
#    elements = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
#    ActionChains(driver).key_down(Keys.CONTROL).click(elements).key_up(Keys.CONTROL).perform()
#
#xpath = "//*[@id=\"ctl00_MainContent_btn_getdata1\"]"
#elements = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
#elements.click()
#comm= ["rice", "wheat", "atta", "gram", "tur", "urad", "moong","masoor","groundnut_oil","mustard_oil", "vanaspati", "soya_oil", "sunflower_oil", "palm_oil", "potato", "onion", "tomato","sugar", "gur", "milk", "tea", "salt"]
#dd_s = start_date[:2]
#mm_s = start_date[3:5]
#yy_s = start_date[6:10]
#dd_e = end_date[:2]
#mm_e = end_date[3:5]
#yy_e = end_date[6:10]
# 
#
#print(dd_s, mm_s, yy_s)
#print(var)
#for i_tab in range(var-var,var-var+1):
#    xpath="//*[@id=\"gv"+str(i_tab)+"\"]"
#    table = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
#
#    with open("prices_"+dd_s+mm_s+yy_s+"_"+dd_e+mm_e+yy_e+"_"+comm[var-1]+".csv", 'w', newline='') as csvfile:
#        wr = csv.writer(csvfile)
#        for row in table.find_elements_by_css_selector('tr'):
#            wr.writerow([d.text for d in row.find_elements_by_css_selector('td')])
#driver.close()


import pandas as pd
import numpy as np

File = "crop_yield_district_india.xlsx"

Data = pd.read_excel(File)

s = Data.iloc[:,0]
y = s[~s.isnull()]

y.iloc[:].shape

dis = y.values

#print(dis)

for d in dis:
    print(d)
    xpath = "//*[@id=\"place\"]"
    elements = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
    elements.click()
    elements.clear() 
    elements.send_keys(d)

    xpath="//*[@id=\"btnfind\"]"
    elements = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
    elements.click()
    time.sleep(5)
    #soup = BeautifulSoup(r.text, 'html.parser')
    #print(soup)
    xpath="//*[@id=\"lat\"]"
    elements = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
    #print(driver.page_source)    
    #soup = BeautifulSoup(driver.page_source, 'html.parser')
    tree = html.fromstring(driver.page_source)
    #print(soup)
    #print(soup.find("div", {"id": "articlebody"}))
    Xpath="//*[@id=\"lng\"]/text()"
    print(tree.xpath(Xpath))
#    elements = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
#    print(elements.text)    


    time.sleep(5)   # Delays for 5 seconds. You can also use a float value.   
