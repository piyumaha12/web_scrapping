from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import pandas as pd

# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

url_amazon = 'https://www.amazon.in/OnePlus-Nord-Sierra-128GB-Storage/product-reviews/B097RDVDL2/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'

# html_text = urlopen(url)
# reviews_txt = open('reviews.txt', 'w')
# list_of_reviews = []


def getweb(html_page=None, url=None):
    '''
    :param enter the url link of 1 review page

    This function returns the link of next page so that the info. can
    be extracted from multiple pages using next page button

    :return Link of next page
    '''

    if url:
        html_page_from_url = urlopen(url, timeout=1000)
        page = BeautifulSoup(html_page_from_url, 'lxml')
    else:
        html_text = html_page
        page = BeautifulSoup(html_text, 'lxml')

    if not page.find('li', {'class': 'a-pagination'}):
        url = 'http://www.amazon.in' + str(page.find('li', {'class': 'a-last'}).find('a')['href'])
        return url
    else:
        print('last page')
        return None


def get_reviews(url, list_of_reviews):
    print(url)
    html_page = urlopen(url)
    html_text = BeautifulSoup(html_page, 'lxml')
    reviews_list = html_text.find_all('div', class_='a-row a-spacing-small review-data')
    page_list = []
    for review in reviews_list:
        x = str(review.text)

        list_of_reviews.append(x)
        page_list.append(x)
    print(len(list_of_reviews))
    return html_page


def save_url(url):
    file = open('url_file_next_page.txt', 'w')
    file.write(url)
    file.close()


# while True:
#     get_reviews(url_amazon)
#     url_amazon = getweb(url=url_amazon)
#     if len(list_of_reviews) % 50 == 0:
#         print(f'{len(list_of_reviews)} review are extracted')
#         file_name = 'reviews_text_file_string' + str(len(list_of_reviews)) + '.txt'
#         with open(file_name, 'w', encoding='utf-8') as file:
#             for review in list_of_reviews:
#                 file.write(f'{review} \n')
#
#         file.close()
#
#     if url_amazon == None:
#         break
#     else:
#         continue

def extract_reviews(url_first = None, url_file_location_name = None, review_file_name = None):
    if url_file_location_name:
        url_open = open(url_file_location_name, 'r').read()
        print('URL successfully loaded')
    else:
        url_open = url_first

    if review_file_name:
        list_of_reviews = open(review_file_name, 'r', encoding= 'utf-8').readlines()
        print(f'Reviews Successfully loaded {len(list_of_reviews)}')
    else:
        list_of_reviews = []
    i = 1
    while True:
        get_reviews(url_open, list_of_reviews)
        url_open = getweb(url=url_open)
        if i % 5 == 0:
            save_url(url_open)
            loc = url_open.rfind('pageNumber') + len('pageNumber')
            end = url_open.rfind('&reviewer')
            no_of_reviews = (int(url_open[loc+1:end])-1)*10
            print(f'{no_of_reviews} review are extracted')
            file_name = 'reviews_oneplus' + str(no_of_reviews) + '.txt'
            with open(file_name, 'w', encoding='utf-8') as file:
                for review in list_of_reviews:
                    file.write(f'{review}')

            file.close()
        i+=1
        if url_amazon == None:
            break
        else:
            continue


# extract_reviews(url_first = url_amazon)
# extract_reviews(url_file_location_name= 'url_file_next_page.txt', review_file_name = 'reviews_oneplus4600.txt')

