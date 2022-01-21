import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

# This header is necessary or else the website will give mod security error
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
}

# Experiment URL 
URL = 'https://insights.blackcoffer.com/how-do-deep-learning-models-predict-old-and-new-drugs-that-are-successfully-treated-in-healthcare/'


def open_url(url, headers=headers):
    R = requests.get(url, headers=headers).text
    soup = BeautifulSoup(R, 'lxml')
    return soup


# Title function
def title_extract(soup, name=None, attrs_type=None, attrs_name=None, string=None):
    if attrs_type == 'class':
        title = soup.find(name, class_=attrs_name, string=string).text
        return title
    elif attrs_type == 'id':
        title = soup.find(name, id=attrs_name, string=string).text
        return title
    elif name or string is True:
        title = soup.find(name, string=string)
        return title
    else:
        print('Please enter something')


# Content extraction
def content_extract(soup, name='h1', attrs_type=None, attrs_name='entry_title', string=None):
    if attrs_type == 'class':
        title = soup.find(name, class_=attrs_name, string=string).text
        return title
    elif attrs_type == 'id':
        title = soup.find(name, id=attrs_name, string=string).text
        return title
    else:
        title = soup.find(name, string=string)
        return title
