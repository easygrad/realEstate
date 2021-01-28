import requests
import re
import time
import random
from selenium import webdriver
from bs4 import BeautifulSoup

short_sec = random.uniform(0.3, 0.5)
mid_sec = random.uniform(0.5, 1.0)
long_sec = random.uniform(2, 3)

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
    if landHouse_types[i]["value"] == "DDDGG" and landHouse_types[i]["aria-pressed"] == "true":
        continue
    elif landHouse_types[i]["aria-pressed"] == "false":
        continue
    elif landHouse_types[i]["value"] == "DDDGG" and landHouse_types[i]["aria-pressed"] == "false":
        landHouse_types_elem[i].click()
    else:
        landHouse_types_elem[i].click()

# 거래방식
trade_types_btn = browser.find_element_by_id("trade_type_filter")
trade_types_deal1 = browser.find_element_by_xpath('//*[@id="trade_type_filter"]/div/div[1]/div/ul/li[2]/label')
trade_types_btn.click()
time.sleep(short_sec)
trade_types_deal1.click()

# 지역: 서울시 > 마포구 > 모든 동
regions_prvnc_btn = browser.find_element_by_xpath('//*[@id="region_filter"]/div/a/span[1]')
regions_city_btn = browser.find_element_by_xpath('//*[@id="region_filter"]/div/a/span[2]')
regions_dong_btn = browser.find_element_by_xpath('//*[@id="region_filter"]/div/a/span[3]')

regions_prvnc_btn.click()
time.sleep(mid_sec)
prvnc_list = browser.find_elements_by_class_name("area_item") # webelement의 텍스트는 .text / elements로 찾으면 list 형태이기 때문에 .text 안됨

# 시험삼아 리스트를 뽑아보면
prvnc_list_arr = []
for prvnc in prvnc_list:
    name = prvnc.find_element_by_class_name("radio_label_district")
    prvnc_list_arr = prvnc_list_arr + [name.text]
print(prvnc_list_arr)

# prvnc_num = print(prvnc_list_arr.index("서울시"))

prvnc_name0 = prvnc_list[0].find_element_by_class_name("radio_label_district") # webelement from webelement 가능함
prvnc_name0.click() # 서울은 일단 0

# 마포구 > 모든동
# city랑 dong btn(버튼)은 안눌러줘도 됨. 자동으로 넘어가기 때문
time.sleep(mid_sec)
city_list = browser.find_elements_by_class_name("area_item")

# 시험삼아 리스트를 뽑아보면
city_list_arr = []
for city in city_list:
    name = city.find_element_by_class_name("radio_label_district")
    city_list_arr = city_list_arr + [name.text]
print(city_list_arr)

city_name12 = city_list[12].find_element_by_class_name("radio_label_district") # webelement from webelement 가능함
city_name12.click() # 마포구는 일단 12

time.sleep(mid_sec)
dong_list = browser.find_elements_by_class_name("area_item")

# # 시험삼아 리스트를 뽑아보면
dong_list_arr = []
for dong in dong_list:
    name = dong.find_element_by_class_name("radio_label_district")
    dong_list_arr = dong_list_arr + [name.text]
print(dong_list_arr)

# dong_num = dong_list_arr.index("공덕동")
# print(dong_num)
# print(len(dong_list_arr))

dong_name0 = dong_list[0].find_element_by_class_name("radio_label_district") # webelement from webelement 가능함
# print(dong_name0.text) # 텍스트 프린트 하려면 클릭 전에 해야 함
dong_name0.click() # 공덕동은 일단 0

time.sleep(mid_sec)

for index in range(len(dong_list_arr)):
    # 도/시 처음부터 다시 클릭해줘야하고, 다 한 다음에는 꺼줘야함
    regions_prvnc_btn.click()
    time.sleep(mid_sec)

    prvnc_list = browser.find_elements_by_class_name("area_item")
    prvnc_name0 = prvnc_list[0].find_element_by_class_name("radio_label_district")
    prvnc_name0.click()
    time.sleep(mid_sec)

    city_list = browser.find_elements_by_class_name("area_item")
    city_name12 = city_list[12].find_element_by_class_name("radio_label_district")
    city_name12.click()
    time.sleep(mid_sec)

    dong_list = browser.find_elements_by_class_name("area_item")
    dong_name = dong_list[index].find_element_by_class_name("radio_label_district")
    print("")
    print("<"*50, dong_name.text, ">"*50)
    print("")
    dong_name.click()

    time.sleep(mid_sec)

    # 매물 리스트
    item_inners = browser.find_elements_by_class_name("item_inner ")
    prev_len = len(item_inners)

    while True:
        browser.execute_script("arguments[0].scrollIntoView(true)", item_inners[-1])
        time.sleep(short_sec)
        curr_len = len(browser.find_elements_by_class_name("item_inner "))
        print(curr_len, prev_len)
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
    
    detail_contents = browser.find_element_by_class_name("detail_panel")
    detail_close = detail_contents.find_element_by_class_name("btn_close")
    detail_close.click()
# 다음 해결할 문제: 네이버 보기가 있는 경우 네이버 보기 클릭   
# 그다음 해결할 문제: 매물 없을 때 넘어가기


# # 매물 리스트
# item_inners = browser.find_elements_by_class_name("item_inner ")
# prev_len = len(item_inners)

# while True:
#     browser.execute_script("arguments[0].scrollIntoView(true)", item_inners[-1])
#     time.sleep(short_sec)
#     curr_len = len(browser.find_elements_by_class_name("item_inner "))
#     print(curr_len, prev_len)
#     if curr_len == prev_len:
#         print("스크롤 완료")
#         print("-"*100)
#         break
#     else:
#         prev_len = curr_len
#         item_inners = browser.find_elements_by_class_name("item_inner ")

# soup = BeautifulSoup(browser.page_source, "lxml")

# items = soup.find_all("div", attrs = {"class":"item_inner"})
# print("매물 개수: ", len(items))
# print("-"*100)

# for index, item in enumerate(items):
#     title = item.find("div", attrs = {"class":"item_title"}).get_text()
#     price_type = item.find("span", attrs = {"class":"type"}).get_text()
#     price = item.find("span", attrs = {"class":"price"}).get_text()
#     spec = item.find("span", attrs = {"class":"spec"}).get_text()
#     detail = browser.find_elements_by_class_name("item_title")[index].click()
#     # detail = item.find("div", attrs = {"class":"item_title"}).click()
#     time.sleep(short_sec)
#     detail_tbl = browser.find_element_by_tag_name("tbody")
#     detail_tbl_num = detail_tbl.find_elements_by_tag_name("tr")[12].find_elements_by_tag_name("td")[1].text
#     detail_url = "https://new.land.naver.com/?articleNo=" + detail_tbl_num
#     print(title)
#     print(price_type, " : ", price)
#     print(spec)
#     print(detail_url)
#     print("-"*100)

# browser.quit()