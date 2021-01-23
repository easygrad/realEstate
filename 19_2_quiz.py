from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time

def landSearch(name):

    url = "https://land.naver.com"
    browser = webdriver.Chrome()
    browser.get(url)
    browser.maximize_window()

    # browser.find_element_by_xpath("//*[@id='queryInputHeader']").click()
    browser.find_element_by_xpath("//*[@id='queryInputHeader']").send_keys(name) # 검색어에 입력
    browser.find_element_by_xpath("//*[@id='queryInputHeader']").send_keys("\n") # 엔터
    # browser.find_element_by_xpath("//*[@id='header']/div[1]/div/div[1]/div/fieldset/a[1]").click() # 검색 클릭
    
    time.sleep(1)

    item_inners = browser.find_elements_by_class_name("item_inner ")
    prev_len = len(item_inners)

    while True:
        browser.execute_script("arguments[0].scrollIntoView(true)", item_inners[-1])
        time.sleep(0.2)
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

    for item in items:
        title = item.find("div", attrs = {"class":"item_title"}).get_text()
        price_type = item.find("span", attrs = {"class":"type"}).get_text()
        price = item.find("span", attrs = {"class":"price"}).get_text()
        spec = item.find("span", attrs = {"class":"spec"}).get_text()
        print(title)
        print(price_type, " : ", price)
        print(spec)
        print("-"*100)
        # price = item.find("")

    browser.quit()

name1 = "리센츠"
landSearch(name1)
