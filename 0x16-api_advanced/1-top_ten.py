#!/usr/bin/python3
"""
    Function to query the Reddit API and returns the titles of the first 10 host posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Custom User"}
    params = {"limit": 10}
    res = requests.get(
          url, headers=headers, params=params, allow_redirects=False)
    data = res.json().get("data").get("children")
    if data:
        for _ in data:
            print(_.get("data").get("title"))
    else:
        print(None)
