"""
Run spider command:
scrapy crawl google_webstore -o google_extension_info.csv
"""
import scrapy
from bs4 import BeautifulSoup


class GoogleWebstoreSpider(scrapy.Spider):
    name = "google_webstore"
    allowed_domains = ["chrome.google.com"]
    start_urls = ['https://chrome.google.com/webstore/sitemap']

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        for url_tag in soup.select('sitemap loc'):
            result = url_tag.text
            yield scrapy.Request(url=result, callback=self.parse_extension_url)

    def parse_extension_url(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        for url_extention in soup.select('url loc'):
            result = url_extention.text
            yield scrapy.Request(url=result, callback=self.parse_page_extension)

    def parse_page_extension(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        url_extension = response.url
        id_extension = url_extension.split('/')[-1]
        name_extension = soup.select_one('h1.Pa2dE').text
        short_description = soup.select_one('.uORbKe p').text

        yield {
            'id_extension': id_extension,
            'name_extension': name_extension,
            'short_description': short_description
        }







# scrapy crawl google_webstore -o google_extension_info.csv

# class GoogleWebstoreSpider(scrapy.Spider):
#     name = "google_webstore"
#     allowed_domains = ["chrome.google.com"]
#     start_urls = ['https://chrome.google.com/webstore/sitemap']

#     def parse(self, response):
#         for url_tag in response.css('sitemap loc'):
#             result = url_tag.get()
#             yield scrapy.Request(url=result, callback=self.parse_extension_url)

#     def parse_extension_url(self, response):
#         for url_extention in response.css('url loc'):
#             result = url_extention.get()
#             yield scrapy.Request(url=result, callback=self.parse_page_extension)

#     def parse_page_extension(self, response):
#         url_extension = response.url
#         id_extension = url_extension.split('/')[-1]
#         name_extension = response.css('h1.Pa2dE::text').get()
#         short_description = response.css('.uORbKe p::text').get()

#         yield {
#             'id_extension': id_extension,
#             'name_extension': name_extension,
#             'short_description': short_description
#         }