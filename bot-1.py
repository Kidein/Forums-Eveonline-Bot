from tabnanny import check
import requests
from urllib.error import HTTPError
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import schedule
import time


url_list1 = list()
url_list2 = list()




def main():
    def check_forum():
        r = requests.get('https://forums.eveonline.com/c/marketplace/sales-ads/')
        soup = BeautifulSoup(r.text, 'lxml')
        return soup

    data = check_forum() 

    tags = data('a', class_='title raw-link raw-topic-link')
    for tag in tags:
        item_url = tag.get('href')
        item_text = tag.text
        url_list1.append(item_text)
        url_list1.append(item_url)    
        
    time.sleep(10)

    def check_forum1():
        r = requests.get('https://forums.eveonline.com/c/marketplace/sales-ads/')
        soup = BeautifulSoup(r.text, 'lxml')
        return soup

    data1 = check_forum1()

    tags = data1('a', class_='title raw-link raw-topic-link')
    for tag in tags:
        item_url = tag.get('href')
        item_text = tag.text
        url_list2.append(item_text)
        url_list2.append(item_url)
    
    if url_list1[2] != url_list2[2]:
        print(url_list2[2])
        print(url_list2[3])
    else:
        print('no new posts')
    
    url_list1.clear()
    url_list2.clear()

schedule.every(10).seconds.do(main)
while True:
    schedule.run_pending()

    