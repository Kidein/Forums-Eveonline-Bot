"""
file with functions
"""
import time

import requests
from bs4 import BeautifulSoup


def get_link(forum_url, links_list):
    """
    with function get_link() we scrape all urls from a forum
    """
    raw_url = requests.get(forum_url)
    soup = BeautifulSoup(raw_url.text, "lxml")
    tags = soup.find_all("a", class_="title raw-link raw-topic-link")
    for tag in tags:
        url = tag.get("href")
        links_list.append(url)
    return links_list


def get_replies(forum_url, replies_list):
    """
    with function get_replies() we scrape number of replies in every topic,
    so we will know if topic is new or not
    """
    raw_url1 = requests.get(forum_url)
    soup = BeautifulSoup(raw_url1.text, "lxml")
    replies = soup.find_all("span", class_="posts")
    for reply in replies:
        replies_list.append(reply.contents)
    return replies_list


async def compare(forum_url):
    """
    with function compare() we compare two lists with links,
    if these lists are not the same (someone updated a forum topic, so it moved to the top),
    we print out the new element from second list
    """
    links_list1, links_list2 = [], []
    state1_list = get_link(forum_url, links_list1)
    time.sleep(60)
    state2_list = get_link(forum_url, links_list2)

    if state1_list[1] == state2_list[1]:
        return []
    return state2_list[1:2]


async def compare_for_new_topics(forum_url):
    """
    with function compare_for_new_topics() we compare two lists with links as we did before,
    but we add another list with amount of replies,
    if the first element equals = 0 in that list, it means that this topic is new
    so it will print a new topic
    """
    replies_list1, links_list01, links_list02 = [], [], []  # pylint: disable=C0301
    first_state_list = get_link(forum_url, links_list01)
    await time.sleep(60)
    second_state_list = get_link(forum_url, links_list02)
    result_list = get_replies(forum_url, replies_list1)
    first_element_list = result_list[1]

    if first_element_list[0] != "0":
        return []
    if first_state_list[1] == second_state_list[1]:
        return []
    return second_state_list[1:2]
