from bs4 import BeautifulSoup


class GoogleMarketPars:
    SITE_URL = 'https://chrome.google.com'

    def make_pars(self, response):
        soup = BeautifulSoup(response, 'lxml')
        for link in soup.select('sitemap'):
            print(link.loc.text, flush=True)
