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

# 매물 리스트 
def findItemList(prvnc, city, dong):

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
    dong_idx = dong_list_arr.index(dong)
    dong_check = dong_elem_list[dong_idx].find_element_by_class_name("radio_label_district")
    dong_check.click()
    time.sleep(mid_sec)

    # 매물 리스트
    item_inners = browser.find_elements_by_class_name("item_inner ")
    prev_len = len(item_inners)
    if prev_len == 0 :
        print("매물 없음")
    else:
        pass

    while True:
        browser.execute_script("arguments[0].scrollIntoView(true)", item_inners[-1])
        time.sleep(short_sec)
        curr_len = len(browser.find_elements_by_class_name("item_inner "))
        if curr_len == prev_len:
            print("스크롤 완료")
            print("-"*100)
            break
        else:
            prev_len = curr_len
            item_inners = browser.find_elements_by_class_name("item_inner ")

    soup = BeautifulSoup(browser.page_source, "lxml")

    items = soup.find_all("div", attrs = {"class":"item_inner"})
    print("매물 개수: ", len(items))
    print("-"*100)

    for index, item in enumerate(items):
        title = item.find("div", attrs = {"class":"item_title"}).get_text()
        price_type = item.find("span", attrs = {"class":"type"}).get_text()
        price = item.find("span", attrs = {"class":"price"}).get_text()
        spec = item.find("span", attrs = {"class":"spec"}).get_text()
        try:
            item_inners[index].find_element_by_class_name("label_area").find_element_by_tag_name("a").click()
            # 네이버에서 보기가 있으면 클릭
        except:
            detail = browser.find_elements_by_class_name("item_title")[index].click()
            # detail = item.find("div", attrs = {"class":"item_title"}).click()
        time.sleep(short_sec)
    
        detail_tbl = browser.find_element_by_tag_name("tbody")
        detail_tbl_num = detail_tbl.find_elements_by_tag_name("tr")[12].find_elements_by_tag_name("td")[1].text
        detail_url = "https://new.land.naver.com/?articleNo=" + detail_tbl_num
        print(title)
        print(price_type, " : ", price)
        print(spec)
        print(detail_url)
        print("-"*100)
        
        if index == 0:
            with open("ItemList.csv", "w", encoding = "utf-8-sig") as f:
                f.write("Title" + "," + "Type" + "," + "Price" + "," + "Spec1" + "," + "Spec2" + "," + "Spec3" + "," + "URL" +"\n")
                price = price.replace(",","")
                f.write(title + "," + price_type + "," + price + "," + spec + "," + detail_url + "\n")
                f.close()
        else:
            with open("ItemList.csv", "a", encoding = "utf-8-sig") as f:
                price = price.replace(",","")
                f.write(title + "," + price_type + "," + price + "," + spec + "," + detail_url + "\n")
                f.close()


def findItemListDetail(prvnc, city, dong):

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
    dong_idx = dong_list_arr.index(dong)
    dong_check = dong_elem_list[dong_idx].find_element_by_class_name("radio_label_district")
    dong_check.click()
    time.sleep(mid_sec)

    # 매물 리스트
    item_inners = browser.find_elements_by_class_name("item_inner ")
    prev_len = len(item_inners)
    if prev_len == 0 :
        print("매물 없음")
    else:
        pass

    while True:
        browser.execute_script("arguments[0].scrollIntoView(true)", item_inners[-1])
        time.sleep(short_sec)
        curr_len = len(browser.find_elements_by_class_name("item_inner "))
        if curr_len == prev_len:
            print("스크롤 완료")
            print("-"*100)
            break
        else:
            prev_len = curr_len
            item_inners = browser.find_elements_by_class_name("item_inner ")

    soup = BeautifulSoup(browser.page_source, "lxml")

    items = soup.find_all("div", attrs = {"class":"item_inner"})
    print("매물 개수: ", len(items))
    print("-"*100)

    for index, item in enumerate(items):
        title = item.find("div", attrs = {"class":"item_title"}).get_text()
        price_type = item.find("span", attrs = {"class":"type"}).get_text()
        price = item.find("span", attrs = {"class":"price"}).get_text()
        spec = item.find("span", attrs = {"class":"spec"}).get_text()
        try:
            item_inners[index].find_element_by_class_name("label_area").find_element_by_tag_name("a").click()
            # 네이버에서 보기가 있으면 클릭
        except:
            detail = browser.find_elements_by_class_name("item_title")[index].click()
            # detail = item.find("div", attrs = {"class":"item_title"}).click()
        time.sleep(short_sec)
    
        detail_tbl = browser.find_element_by_tag_name("tbody")
        detail_tbl_fee = detail_tbl.find_elements_by_tag_name("tr")[6].find_elements_by_tag_name("td")[1].text
        detail_tbl_num = detail_tbl.find_elements_by_tag_name("tr")[12].find_elements_by_tag_name("td")[1].text
        detail_fee_deposit = 
        detail_fee_rent
        detail_url = "https://new.land.naver.com/?articleNo=" + detail_tbl_num
        print(title)
        print(price_type, " : ", price)
        print(spec)
        print(detail_url)
        print("-"*100)
        
        if index == 0:
            with open("ItemList.csv", "w", encoding = "utf-8-sig") as f:
                f.write("Title" + "," + "Type" + "," + "Price" + "," + "Spec1" + "," + "Spec2" + "," + "Spec3" + "," + "URL" +"\n")
                price = price.replace(",","")
                f.write(title + "," + price_type + "," + price + "," + spec + "," + detail_url + "\n")
                f.close()
        else:
            with open("ItemList.csv", "a", encoding = "utf-8-sig") as f:
                price = price.replace(",","")
                f.write(title + "," + price_type + "," + price + "," + spec + "," + detail_url + "\n")
                f.close()

# findPrvncList()
# findCityList("서울시")
# findDongList("서울시", "마포구")
findItemList("강원도", "원주시", "단계동")