"""
file with functions
"""
import asyncio
import time

import discord
import requests
from bs4 import BeautifulSoup


class ForumTracker:
    def get_link(self, forum_url, links_list):
        """
        with function get_link() we scrape all urls from a forum
        """
        links_list = []
        raw_url = requests.get(forum_url)
        soup = BeautifulSoup(raw_url.text, "lxml")
        tags = soup.find_all("a", class_="title raw-link raw-topic-link")
        for tag in tags:
            url = tag.get("href")
            links_list.append(url)
        return links_list

    async def compare(self, forum_url):
        """
        with function compare() we compare two lists with links,
        if these lists are not the same (someone updated a forum topic, so it moved to the top),
        we print out the new element from second list
        """
        links_list1, links_list2 = [], []
        state1_list = self.get_link(forum_url, links_list1)
        await asyncio.sleep(10)
        state2_list = self.get_link(forum_url, links_list2)

        if state1_list[1] == state2_list[1]:
            print("no changes")
            return []
        return state2_list[1:2]


Bot = ForumTracker()
asyncio.run(Bot.compare("https://forums.eveonline.com/c/marketplace/sales-ads/55"))
