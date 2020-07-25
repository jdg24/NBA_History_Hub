import config
import requests
from bs4 import BeautifulSoup


class BaseCrawler:
    def get_html(self, url):
        return requests.get(url)

    def get_response_text(self, response):
        return response.text

    def get_soup(self, response):
        return BeautifulSoup(response, features=config.bs4_parser)
