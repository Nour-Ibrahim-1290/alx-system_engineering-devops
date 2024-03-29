#!/usr/bin/python3
"""
    Function to query the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Custom User"}
    res = requests.get(url, headers=headers)
    data = res.json().get("data").get("subscribers")
    return data if data else 0
