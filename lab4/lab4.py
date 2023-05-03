import requests
from bs4 import BeautifulSoup


def get_ukd_specializations():
    url = 'https://ukd.edu.ua'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    content_div = soup.find(class_='col-lg-9 col-md-12')
    ul = content_div.ul
    links = ul.find_all('a')
    for link in links:
        if link.text == 'Спеціальності':
            continue
        print(link.text)


if __name__ == '__main__':
    get_ukd_specializations()