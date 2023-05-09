#!/usr/bin/python3
"""get a lit of suscribber on a subreddit"""
import requests
import sys


def number_of_subscribers(subreddit):
    """number of suscribers"""
    if subreddit is None or type(subreddit) != str:
        return (0)
    url = "https://reddit.com/r/{}/about.json".format(
            subreddit)
    headers = {'User-Agent': 'API project'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if (response.status_code != 200):
        return (0)
    sus = response.json.get('suscribers', 0)
    return (sus)
