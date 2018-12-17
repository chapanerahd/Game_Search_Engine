# -*- coding: utf-8 -*-

import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from langdetect import detect


def check_connection(url):
    # Returns the response status of the URL
    try:
        return requests.get(url).status_code
    except Exception as e:
        return e


def get_website_content(url):
    # Parse the html text of the URL
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    return soup


def parse_url(url):
    # Check if the format of the URL is correct
    parsed_url = urlparse(url)
    if parsed_url.scheme == '':
        url = "http://www." + url
        parsed_url = urlparse(url)
    return parsed_url.scheme + "://" + parsed_url.netloc + "/"


def get_language(sentence):
    # Detect the langauge of the string
    try:
        return detect(sentence)
    except Exception as e:
        return None
