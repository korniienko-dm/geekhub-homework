"""
2. Викорисовуючи requests, заходите на ось цей сайт "https://www.expireddomains.net/deleted-domains/"
(з ним будьте обережні), вибираєте будь-яку на ваш вибір доменну зону і парсите список  доменів - їх
там буде десятки тисяч (звичайно ураховуючи пагінацію). Всі отримані значення зберігти в CSV файл.
"""
import csv
import time
from pathlib import Path
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from json.decoder import JSONDecodeError
import requests


class ParseExpiredDomains:
    """A class for parsing expired domains from a website
    Attributess:
        base_url (str): The base URL of the website.
        base_dir (Path): The base directory where the CSV file will be saved.
        csv_file_path (str): The relative path to the CSV file.
        user_agent (dict): The user agent for making HTTP requests.
    Methods:
        __init__: Initializes the ParseExpiredDomains instance.
        pars_page_data: Parses data from a given URL.
        save_to_csv: Saves data to a CSV file.
        main: The main method for running the parsing process.
    """

    def __init__(self, base_url, base_dir, csv_save_dir_path, user_agent):
        """Initialize ParseExpiredDomains."""
        self.base_url = base_url
        self.base_dir = base_dir
        self.csv_file_path = csv_save_dir_path
        self.user_agent = user_agent

    def pars_page_data(self, parse_url):
        """Parse data from a given URL."""
        page_content = []
        response = requests.get(parse_url, headers=self.user_agent)
        response.raise_for_status()
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            field_domains = soup.select('.field_domain a')
            if not field_domains:
                return False, 'Element: ".field_domain a" was not found on the page.'
            for field_domain in field_domains:
                page_content.append(field_domain.text)
            next_page_element = soup.select_one('.next')
            next_page_path = next_page_element['href'] if next_page_element else None
            return True, page_content, next_page_path
        return False, response.status_code

    @staticmethod
    def save_to_csv(data_list, save_path, filename='expired_domains_list.csv'):
        """Save data to a CSV file."""
        file_exists = Path(save_path / filename).is_file()
        file_path = save_path / filename
        with open(file_path, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['site_url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            for item in data_list:
                writer.writerow({'site_url': item})

    def main(self):
        """The main method for running the parsing process."""
        url_page_list = [self.base_url + '/expired-domains']
        run_pars = True
        delay_seconds = 5
        while run_pars:
            try:
                print(f"Delay before request is: {delay_seconds} seconds. Wait...")
                time.sleep(delay_seconds)
                response_from_page = self.pars_page_data(parse_url=url_page_list[-1])
                if not response_from_page[0]:
                    return f"Error: {response_from_page[1]}"
                print(f"Start parse page: {url_page_list[-1]}")
                status_parse_page = response_from_page[0]
                data_page = response_from_page[1]
                next_page = response_from_page[2]
                if status_parse_page:
                    url_page_list.append(urljoin(self.base_url, next_page))
                    self.save_to_csv(data_list=data_page, save_path=self.base_dir / self.csv_file_path)
                else:
                    run_pars = False
                    print(response_from_page[1])
                    break
            except requests.exceptions.RequestException as text_error:
                print(f"Error in request: {text_error}")
                break
            except JSONDecodeError as text_error:
                print(f"Error decoding JSON: {text_error}")
                break
            except Exception as text_error:
                print(f"Error: {text_error}")
                break
        return f"The work is done. Pages processed: {len(url_page_list)}"


if __name__ == '__main__':
    # 1. Without registration, expireddomains.net allows viewing only 325 entries.
    # 2. Access to the system is granted through a login and password.
    # 3. expireddomains.net: "The member area requires a session cookie to be stored on your computer."
    # 4. expireddomains.net: "The cookie is only valid for the time of your session and will be
    #    automatically deleted by your browser when you close it."
    # 5. During user verification, a code is also sent to the email address provided during registration.
    # 6. Using the "successfully authenticated cookie" in the header:
    #    'Cookie': 'ExpiredDomainssessid=SqZQVIZli4kHWiseGiel8Zd-BNJZvDd0hHWij%2CrhbTNFnwArjbAAL2u0nlHpg1ZjoLOoLpqRAYsJ8D1ZHcfDjksESu2qsFYdQh0KntEG4u--ary0zaThv4nfdj5apikA'
    #
    #    It is possible to successfully analyze all values ​​from a domain zone. With a 5 second delay between requests.
    # 7. The "Cookie" ceases to be active for use 3-4 hours after the last usage.
    
    BASE_DIR = Path(__file__).resolve().parent
    CSV_FILE_PATH = 'task_2_files'
    USER_AGENT = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0'}
    BASE_URL = 'https://www.expireddomains.net' 
    
    parse_domains = ParseExpiredDomains(base_url=BASE_URL, base_dir=BASE_DIR, csv_save_dir_path=CSV_FILE_PATH, user_agent=USER_AGENT)
    print(parse_domains.main())
