"""
file with functions
"""

import requests
from bs4 import BeautifulSoup


class Meow:
    #     def __init__(self) -> None:
    #         self.links_list = []

    def get_link(self, forum_url):
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
        # return links_list
        print(links_list)


a = Meow()
a.get_link("https://forums.eveonline.com/c/marketplace/sales-ads/55")
