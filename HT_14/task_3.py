"""
3.
http://quotes.toscrape.com/ - написати скрейпер для збору всієї доступної
інформації про записи: цитата, автор, інфа про автора тощо. 
- збирається інформація з 10 сторінок сайту.
- зберігати зібрані дані у CSV файл
"""
import csv
from pathlib import Path
import requests
from bs4 import BeautifulSoup


class ParsQuotes:
    """
    A class for scraping and parsing quotes from a website and saving the data to a CSV file.

    Attributes:
    - base_url (str): The base URL of the website.
    - csv_file_path (str): The file path to save the CSV file.

    Methods:
    - get_author_information(base_url: str, author_url: str) -> List[Dict[str, str]]:
        Get information about the author from the author's URL.

    - scrape_page(base_url: str, work_url: str) -> List[Dict[str, str]] or None:
        Scrape quotes and related information from a given page URL.

    - get_all_url(base_url: str) -> List[str]:
        Get a list of all page URLs by navigating through the paginated structure.

    - save_to_csv(data: List[Dict[str, str]], csv_filename: str) -> None:
        Save the parsed data to a CSV file.

    - main() -> None:
        The main method that orchestrates the scraping, parsing, and saving to CSV.
    """

    def __init__(self, base_url, csv_file_path):
        self.base_url = base_url
        self.csv_file_path = csv_file_path


    @staticmethod
    def get_author_information(base_url: str, author_url: str):
        """
        Get information about the author from the author's URL.
        """              
        info_about_author = list()
        responce = requests.get(base_url + author_url)
        soup = BeautifulSoup(responce.text, 'lxml')
        author_inf_conainner = soup.select_one('.author-details')

        author_born_date = author_inf_conainner.select_one('.author-born-date').text
        author_born_location = author_inf_conainner.select_one('.author-born-location').text
        author_description_info = author_inf_conainner.select_one('.author-description').text
        author_description = author_description_info.lstrip().rstrip().replace('\n', '')

        info_about_author.append({'author_born_date': author_born_date,
                                'author_born_location': author_born_location,
                                'author_description': author_description})
        return info_about_author


    def scrape_page(self, base_url: str, work_url: str):
        """
        Scrape quotes and related information from a given page URL.
        """  
        response = requests.get(work_url)
        response.encoding = 'utf-8'
        if response.status_code == 200:
            print(f"Scraping page: {work_url}")
            soup = BeautifulSoup(response.text, 'lxml')

            quotes = soup.select('.quote')

            data = list()
            for quote in quotes:
                text = quote.select_one('.text').text[1:-1]
                author = quote.select_one('span .author').text
                about_author_url = quote.select_one('.quote span a')['href']

                tegs = quote.select('.tag')
                tegs_list = list()
                for i in tegs:
                    tegs_list.append(i.text)
                tegs_quote = ", ".join(tegs_list)

                info_about_author = self.get_author_information(base_url=base_url, author_url=about_author_url)

                data.append({'text': text,
                            'author': author,
                            'author_born_date': info_about_author[0]['author_born_date'],
                            'author_born_location': info_about_author[0]['author_born_location'],
                            'author_description': info_about_author[0]['author_description'],
                            'about_author_url': about_author_url,
                            'tegs': tegs_quote})
            return data

        else:
            print(f"Error: Unable to fetch data from {work_url}")
            return None


    @staticmethod
    def get_all_url(base_url: str):
        """
        Get a list of all page URLs by navigating through the paginated structure.
        """
        page_url = list()
        page_url.append(base_url)

        while True:
            response = requests.get(page_url[-1])
            soup = BeautifulSoup(response.text, 'lxml')
            links_next_page = soup.select_one("nav .pager .next a")

            if links_next_page:
                links_next_page = links_next_page.get('href')
                page_url.append(page_url[0] + links_next_page)
            else:
                break

        return page_url


    @staticmethod
    def save_to_csv(data, csv_filename):
        """
        Save the parsed data to a CSV file.
        """
        fieldnames = ['text',
                    'author',
                    'author_born_date',
                    'author_born_location',
                    'author_description',
                    'about_author_url',
                    'tegs']

        with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames, quoting=csv.QUOTE_NONNUMERIC)
            writer.writeheader()

            for ellement in data:
                writer.writerow(ellement)


    def main(self):
        """
        The main method that orchestrates the scraping, parsing, and saving to CSV.
        """
        data = list()
        urls_list = self.get_all_url(base_url=self.base_url)

        for url in urls_list:
            page_data = self.scrape_page(base_url=self.base_url, work_url=url)
            if page_data:
                data.extend(page_data)

        self.save_to_csv(data=data, csv_filename=self.csv_file_path)


if __name__ == "__main__":
    WORK_BASE_DIR = Path(__file__).resolve().parent
    SAVE_CSV = 'task_3_file/quotes_data.csv'
    scraping = ParsQuotes(base_url='http://quotes.toscrape.com', csv_file_path=WORK_BASE_DIR / SAVE_CSV)
    scraping.main()
