# 다가구 주택 검색: 부동산 홈 -> 매물 -> 빌라·주택 -> 단독/다가구(True, 나머지는 False)
# 지역: ex) 서울시 > 마포구 > 공덕동 
# 거래방식: 매매
# 가격대: 4억원 ~ 14억원
# 기타옵션

import requests
import re
import time
from selenium import webdriver
from bs4 import BeautifulSoup

# 다가구 주택 검색
url = "https://land.naver.com"
browser = webdriver.Chrome()
browser.get(url)
browser.maximize_window()

mapOpen_elem = browser.find_element_by_xpath('//*[@id="lnb"]/div/ul/li[2]')
mapOpen_elem.click()

landHouse_elem = browser.find_element_by_xpath('//*[@id="wrap"]/div[1]/a[2]')
landHouse_elem.click()

soup = BeautifulSoup(browser.page_source, "lxml")
landHouse_types = soup.find_all("button", attrs = {"class":"filter_type"})
landHouse_types_elem = browser.find_elements_by_class_name("filter_type")

for i in range(len(landHouse_types)):
    if landHouse_types[i]["value"] == "DDDGG":
        continue
    elif landHouse_types[i]["aria-pressed"] == "false":
        continue
    else:
        landHouse_types_elem[i].click()

# 거래방식
trade_types_btn = browser.find_element_by_id("trade_type_filter")
trade_types_deal1 = browser.find_element_by_xpath('//*[@id="trade_type_filter"]/div/div[1]/div/ul/li[2]/label')
trade_types_btn.click()
time.sleep(0.2)
trade_types_deal1.click()

# 지역: 서울시 > 마포구 > 공덕동
regions_prvnc_btn = browser.find_element_by_xpath('//*[@id="region_filter"]/div/a/span[1]')
regions_city_btn = browser.find_element_by_xpath('//*[@id="region_filter"]/div/a/span[2]')
regions_dong_btn = browser.find_element_by_xpath('//*[@id="region_filter"]/div/a/span[3]')

regions_prvnc_btn.click()
time.sleep(0.5) # 동작형이기 때문에 일정시간 기다려줘야함
prvnc_list = browser.find_elements_by_class_name("area_item") # webelement의 텍스트는 .text / elements로 찾으면 list 형태이기 때문에 .text 안됨
# prvnc_name0 = prvnc_list[0].find_element_by_class_name("radio_label_district") # webelement from webelement 가능함
# prvnc_name0.click() # 서울은 일단 0, 나중에 for 문으로 여러개 적용 가능함

# 시험삼아 리스트를 뽑아보면
for prvnc in prvnc_list:
    name = prvnc.find_element_by_class_name("radio_label_district")
    print(name.text)

