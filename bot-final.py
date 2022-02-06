import requests
from bs4 import BeautifulSoup
import schedule
import time


url_list1 = []
url_list2 = []


def check_forum():
        r = requests.get('https://forums.eveonline.com/c/marketplace/sales-ads/')
        soup = BeautifulSoup(r.text, 'lxml')
        return soup


def main(listname):
    check_forum()
    data = check_forum() 
    tags = data('a', class_='title raw-link raw-topic-link')
    for tag in tags:
        item_url = tag.get('href')
        item_text = tag.text
        listname.append(item_text)
        listname.append(item_url) 
    return(listname)


def checking_on_sales():
    testlist1 = main(url_list1)
    time.sleep(10)
    testlist2 = main(url_list2)



    if testlist1[2] != testlist2[2]:
        print(testlist2[2])
        print(testlist2[3])
    else:
        print('no new posts \n')
    
    url_list1.clear()
    url_list2.clear()   


schedule.every(10).seconds.do(checking_on_sales)
while True:
    schedule.run_pending()

    