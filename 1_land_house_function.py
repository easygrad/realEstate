import requests
import re
import time
import random
from selenium import webdriver
from bs4 import BeautifulSoup


def findPrvncList():

    short_sec = random.uniform(0.3, 0.5)
    mid_sec = random.uniform(0.5, 1.0)
    long_sec = random.uniform(2, 3)

    url = "https://land.naver.com"
    browser = webdriver.Chrome()
    browser.get(url)
    browser.maximize_window()

    mapOpen_elem = browser.find_element_by_xpath('//*[@id="lnb"]/div/ul/li[2]')
    mapOpen_elem.click()

    landHouse_elem = browser.find_element_by_xpath('//*[@id="wrap"]/div[1]/a[2]')
    landHouse_elem.click()

    # 단독/다가구 선택: DDDGG(단독다가구)
    soup = BeautifulSoup(browser.page_source, "lxml")
    landHouse_types = soup.find_all("button", attrs = {"class":"filter_type"})

    landHouse_types_elem = browser.find_elements_by_class_name("filter_type")

    for i in range(len(landHouse_types)):
        if landHouse_types[i]["value"] == "DDDGG" and landHouse_types[i]["aria-pressed"] == "true":
            continue
        elif landHouse_types[i]["aria-pressed"] == "false":
            continue
        elif landHouse_types[i]["value"] == "DDDGG" and landHouse_types[i]["aria-pressed"] == "false":
            landHouse_types_elem[i].click()
        else:
            landHouse_types_elem[i].click()

    # 거래방식: 매매(dea1)
    trade_types_btn = browser.find_element_by_id("trade_type_filter")
    trade_types_deal1 = browser.find_element_by_xpath('//*[@id="trade_type_filter"]/div/div[1]/div/ul/li[2]/label')
    trade_types_btn.click()
    time.sleep(short_sec)
    trade_types_deal1.click()
    time.sleep(short_sec)

    # 지역: 광역시/도
    regions_prvnc_btn = browser.find_element_by_xpath('//*[@id="region_filter"]/div/a/span[1]')
    regions_prvnc_btn.click()
    time.sleep(mid_sec)

    prvnc_elem_list = browser.find_elements_by_class_name("area_item")
    prvnc_list_arr = []
    for prvnc_elem in prvnc_elem_list:
        name = prvnc_elem.find_element_by_class_name("radio_label_district")
        prvnc_list_arr = prvnc_list_arr + [name.text]
    print(prvnc_list_arr)


# 시/구 리스트 
def findCityList(prvnc):

    short_sec = random.uniform(0.3, 0.5)
    mid_sec = random.uniform(0.5, 1.0)
    long_sec = random.uniform(2, 3)

    url = "https://land.naver.com"
    browser = webdriver.Chrome()
    browser.get(url)
    browser.maximize_window()

    mapOpen_elem = browser.find_element_by_xpath('//*[@id="lnb"]/div/ul/li[2]')
    mapOpen_elem.click()

    landHouse_elem = browser.find_element_by_xpath('//*[@id="wrap"]/div[1]/a[2]')
    landHouse_elem.click()

    # 단독/다가구 선택: DDDGG(단독다가구)
    soup = BeautifulSoup(browser.page_source, "lxml")
    landHouse_types = soup.find_all("button", attrs = {"class":"filter_type"})

    landHouse_types_elem = browser.find_elements_by_class_name("filter_type")

    for i in range(len(landHouse_types)):
        if landHouse_types[i]["value"] == "DDDGG" and landHouse_types[i]["aria-pressed"] == "true":
            continue
        elif landHouse_types[i]["aria-pressed"] == "false":
            continue
        elif landHouse_types[i]["value"] == "DDDGG" and landHouse_types[i]["aria-pressed"] == "false":
            landHouse_types_elem[i].click()
        else:
            landHouse_types_elem[i].click()

    # 거래방식: 매매(dea1)
    trade_types_btn = browser.find_element_by_id("trade_type_filter")
    trade_types_deal1 = browser.find_element_by_xpath('//*[@id="trade_type_filter"]/div/div[1]/div/ul/li[2]/label')
    trade_types_btn.click()
    time.sleep(short_sec)
    trade_types_deal1.click()
    time.sleep(short_sec)

    # 지역: 광역시/도
    regions_prvnc_btn = browser.find_element_by_xpath('//*[@id="region_filter"]/div/a/span[1]')
    regions_prvnc_btn.click()
    time.sleep(mid_sec)

    prvnc_elem_list = browser.find_elements_by_class_name("area_item")
    prvnc_list_arr = []
    for prvnc_elem in prvnc_elem_list:
        name = prvnc_elem.find_element_by_class_name("radio_label_district")
        prvnc_list_arr = prvnc_list_arr + [name.text]
    prvnc_idx = prvnc_list_arr.index(prvnc)
    prvnc_check = prvnc_elem_list[prvnc_idx].find_element_by_class_name("radio_label_district") # webelement from webelement 가능함
    prvnc_check.click()
    time.sleep(mid_sec)

    city_elem_list = browser.find_elements_by_class_name("area_item")

    city_list_arr = []
    for city_elem in city_elem_list:
        name = city_elem.find_element_by_class_name("radio_label_district")
        city_list_arr = city_list_arr + [name.text]
    print(city_list_arr)

# 동 리스트 
def findDongList(prvnc, city):

    short_sec = random.uniform(0.3, 0.5)
    mid_sec = random.uniform(0.5, 1.0)
    long_sec = random.uniform(2, 3)

    url = "https://land.naver.com"
    browser = webdriver.Chrome()
    browser.get(url)
    browser.maximize_window()

    mapOpen_elem = browser.find_element_by_xpath('//*[@id="lnb"]/div/ul/li[2]')
    mapOpen_elem.click()

    landHouse_elem = browser.find_element_by_xpath('//*[@id="wrap"]/div[1]/a[2]')
    landHouse_elem.click()

    # 단독/다가구 선택: DDDGG(단독다가구)
    soup = BeautifulSoup(browser.page_source, "lxml")
    landHouse_types = soup.find_all("button", attrs = {"class":"filter_type"})

    landHouse_types_elem = browser.find_elements_by_class_name("filter_type")

    for i in range(len(landHouse_types)):
        if landHouse_types[i]["value"] == "DDDGG" and landHouse_types[i]["aria-pressed"] == "true":
            continue
        elif landHouse_types[i]["aria-pressed"] == "false":
            continue
        elif landHouse_types[i]["value"] == "DDDGG" and landHouse_types[i]["aria-pressed"] == "false":
            landHouse_types_elem[i].click()
        else:
            landHouse_types_elem[i].click()

    # 거래방식: 매매(dea1)
    trade_types_btn = browser.find_element_by_id("trade_type_filter")
    trade_types_deal1 = browser.find_element_by_xpath('//*[@id="trade_type_filter"]/div/div[1]/div/ul/li[2]/label')
    trade_types_btn.click()
    time.sleep(short_sec)
    trade_types_deal1.click()
    time.sleep(short_sec)

    # 지역: 광역시/도
    regions_prvnc_btn = browser.find_element_by_xpath('//*[@id="region_filter"]/div/a/span[1]')
    regions_prvnc_btn.click()
    time.sleep(mid_sec)

    prvnc_elem_list = browser.find_elements_by_class_name("area_item")
    prvnc_list_arr = []
    for prvnc_elem in prvnc_elem_list:
        name = prvnc_elem.find_element_by_class_name("radio_label_district")
        prvnc_list_arr = prvnc_list_arr + [name.text]
    prvnc_idx = prvnc_list_arr.index(prvnc)
    prvnc_check = prvnc_elem_list[prvnc_idx].find_element_by_class_name("radio_label_district")
    prvnc_check.click()
    time.sleep(mid_sec)

    city_elem_list = browser.find_elements_by_class_name("area_item")

    city_list_arr = []
    for city_elem in city_elem_list:
        name = city_elem.find_element_by_class_name("radio_label_district")
        city_list_arr = city_list_arr + [name.text]
    city_idx = city_list_arr.index(city)
    city_check = city_elem_list[city_idx].find_element_by_class_name("radio_label_district")
    city_check.click()
    time.sleep(mid_sec)

    dong_elem_list = browser.find_elements_by_class_name("area_item")

    dong_list_arr = []
    for dong_elem in dong_elem_list:
        name = dong_elem.find_element_by_class_name("radio_label_district")
        dong_list_arr = dong_list_arr + [name.text]
    print(dong_list_arr)

findDongList("서울시", "강남구")