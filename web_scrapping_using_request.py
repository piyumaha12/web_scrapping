from bs4 import BeautifulSoup
import requests
# from urllib.request import urlopen

# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

url_amazon = 'https://www.amazon.in/Infinity-Glide-510-Headphone-Equalizer/product-reviews/B0873L7J6X/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'

# html_text = urlopen(url)
# reviews_txt = open('reviews.txt', 'w')
list_of_reviews = []


def getweb(html_page=None, url=None):
    '''
    :param enter the url link of 1 review page

    This function returns the link of next page so that the info. can
    be extracted from multiple pages using next page button

    :return Link of next page
    '''
    if url:
        html_page_from_url = requests.get(url).text
        page = BeautifulSoup(html_page_from_url, 'lxml')
        # print(page)
    else:
        html_text = html_page
        page = BeautifulSoup(html_text, 'lxml')

    if not page.find('li', {'class': 'a-pagination'}):
        url = 'http://www.amazon.in' + str(page.find('li', {'class': 'a-last'}).find('a')['href'])
        return url
    else:
        print('last page')
        return None


def get_reviews(url):
    print(url)
    html_page = requests.get(url).text
    html_text = BeautifulSoup(html_page, 'lxml')
    reviews_list = html_text.find_all('div', class_='a-row a-spacing-small review-data')
    page_list = []
    for review in reviews_list:
        x = review.text

        list_of_reviews.append(x)
        page_list.append(x)
    print(len(list_of_reviews))
    return html_page




# while True:
#     get_reviews(url_amazon)
#     url_amazon = getweb(url=url_amazon)
#     if len(list_of_reviews) % 100 == 0:
#         print(f'{len(list_of_reviews)} review are extracted')
#         file_name = 'reviews_text_file_using_request' + str(len(list_of_reviews)) + '.txt'
#         file = open(file_name, 'w', encoding='utf-8')
#         file.write(str(list_of_reviews))
#         file.close()
#
#     if url_amazon == None:
#         break
#     else:
#         continue

