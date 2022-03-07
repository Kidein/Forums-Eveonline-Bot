import time

import requests
import schedule
from bs4 import BeautifulSoup


def get_info(forum_url, list_name):
    r = requests.get(forum_url)
    soup = BeautifulSoup(r.text, "lxml")
    tags = soup.find_all("a", class_="title raw-link raw-topic-link")
    for tag in tags:
        item_url = tag.get("href")
        list_name.append(item_url)
    return list_name


def compare(forum_url):
    state1_list, state2_list = [], []
    list1 = get_info(forum_url, state1_list)
    time.sleep(60)
    list2 = get_info(forum_url, state2_list)

    if list1[1] != list2[1]:
        final1 = list2[1:2].copy()
        return final1
    else:
        return []