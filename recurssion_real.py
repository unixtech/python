# from functools import cache, lru_cache
import requests


cache = dict()


def get_article_from_server(url: str) -> str:
    print("Fetching article from server")
    response = requests.get(url)
    return response.text


def get_article(url: str) -> str:
    print("Getting Article ")
    if url not in cache:
        cache[url] = get_article_from_server(url)
    return cache[url]


get_article('https://realpython.com/sorting-algorithm-python')
get_article('https://realpython.com/sorting-algorithm-python')
