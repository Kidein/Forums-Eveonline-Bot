import time

import requests
import schedule
from bs4 import BeautifulSoup


def get_link(forum_url, links_list):
    r = requests.get(forum_url)
    soup = BeautifulSoup(r.text, "lxml")
    tags = soup.find_all("a", class_="title raw-link raw-topic-link")
    for tag in tags:
        url = tag.get("href")
        links_list.append(url)
    return links_list


def get_replies(forum_url, replies_list):
    r = requests.get(forum_url)
    soup = BeautifulSoup(r.text, "lxml")
    replies = soup.find_all("span", class_="posts")
    for reply in replies:
        replies_list.append(reply.contents)


def compare(forum_url):
    links_list1, links_list2 = [], []
    state1_list = get_link(forum_url, links_list1)
    time.sleep(60)
    state2_list = get_link(forum_url, links_list2)

    if state1_list[1] != state2_list[1]:
        return state2_list[1:2]
    else:
        return []


def compare_for_new_topics(forum_url):
    replies_list1, links_list01, links_list02 = [], [], []
    first_state_list = get_link(forum_url, links_list01)
    time.sleep(60)
    second_state_list = get_link(forum_url, links_list02)
    replies_list = get_replies(forum_url, replies_list1)
    x = replies_list[1]
    if x[0] == "0":
        if first_state_list[1] != second_state_list[1]:
            return second_state_list[1:2]
        else:
            return []
    else:
        return []
