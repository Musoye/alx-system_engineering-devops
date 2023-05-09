#!/usr/bin/python3
"""get a lit of suscribber on a subreddit"""
import requests
import sys


def number_of_subscribers(subreddit):
    """number of suscribers"""
    sus - sys.argv[1]
    if sus is None or type
    url = "https://reddit.com/r/{}/about.json".format(
            sys.argv[1])
    headers = {'User-Agent': 'API project'}
    response = requests.get(url, headers=headers, allow_redirects=False)
