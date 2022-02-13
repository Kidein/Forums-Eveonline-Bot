import time

import requests
import schedule
from bs4 import BeautifulSoup

last_topic_list = []


def get_info(forum_url, list_name):
    r = requests.get(forum_url)
    soup = BeautifulSoup(r.text, "lxml")
    tags = soup.find_all("a", class_="title raw-link raw-topic-link")
    for tag in tags:
        item_url = tag.get("href")
        item_text = tag.text
        list_name.append(item_text)
        list_name.append(item_url)
    return list_name


def print_last_topic(forum_url, list_name):
    get_info(forum_url, list_name)
    print(list_name[2], "\n ")
    print(list_name[3], "\n ")
    list_name.clear()


def compare(forum_url):
    state1_list, state2_list, final_list = [], [], []
    list1 = get_info(forum_url, state1_list)
    time.sleep(120)
    list2 = get_info(forum_url, state2_list)

    if list1[2] != list2[2]:
        final1 = list2[2:4].copy()
        # print(list2[2], "\n ")
        # print(list2[3], "\n ")
        return final1
    else:
        print("no new posts \n")

    state1_list.clear()
    state2_list.clear()


def compare_on_time(forum_url):
    schedule.every(1).seconds.do(compare, forum_url)
    while True:
        schedule.run_pending()

if message.content.startswith('!start'):
    whilte True:
    data = compare("https://forums.eveonline.com/c/marketplace/sales-ads/")
    for line in data:
        await message.channel.send(line)
print(data)


