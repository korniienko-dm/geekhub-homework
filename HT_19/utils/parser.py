import requests
import time
import random


class SearsProductScraping:
    """A class for scraping product information from Sears API."""

    def __init__(self, product_id):
        """Initialize the SearsProductScraping object."""
        self.product_id = product_id

    def get_format_id(self):
        """Format the product ID."""
        api_product_id = self.product_id.split("-")[1]
        api_product_id.strip()
        api_product_id.upper()
        return api_product_id

    def get_api_link(self):
        """Generate a link for an API request."""
        product_id = self.get_format_id()
        api_link = f'https://www.sears.com/api/sal/v3/products/details/{product_id}?storeName=Sears&memberStatus=G&zipCode=10101'
        return api_link

    @staticmethod
    def get_cookies():
        """Get cookies for Sears API requests."""
        cookies = {
            'forterToken': '490419e952674df3a2e10559041ae1ad_1702069808413_265_UDF43-m4_13ck',
            'irp': 'a5f52493-1f66-4831-8720-e74613205612|LMlI4mAJjZWKoleMAl0O%2FGDAIIWQSeakKXIGUXLCQtA%3D|G|4d001f3f-ff56-4b1a-9db6-0a8345cf4732|0|NO_SESSION_TOKEN_COOKIE',
            'OptanonConsent': 'isIABGlobal=false&datestamp=Fri+Dec+08+2023+23%3A10%3A12+GMT%2B0200+(%D0%92%D0%BE%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B0%D1%8F+%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=202209.1.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1%2CSPD_BG%3A1&geolocation=UA%3B71&AwaitingReconsent=false',
            'cf_clearance': 'Lo5jTovx.bYtEdyWcAo7BaYPccHOl.BQt2_NS1p0NFY-1702069810-0-1-b1649aee.5c0d64ee.251cda29-0.2.1702069810',
            'OptanonAlertBoxClosed': '2023-12-08T21:10:12.296Z',
            '_ga_L7QE48HF7H': 'GS1.1.1702067233.5.1.1702069942.60.0.0',
            '_ga': 'GA1.2.33524544.1701891048',
            'initialTrafficSource': 'utmcsr=(direct)|utmcmd=(none)|utmccn=(not set)',
            '__utmzzses': '1',
            '_gcl_au': '1.1.264973487.1701891050',
            '_clck': '1illh45%7C2%7Cfhb%7C0%7C1435',
            '_fbp': 'fb.1.1701891051484.773555828',
            '__gsas': 'ID=e49fc0cbca6f8fda:T=1701891050:RT=1701891050:S=ALNI_MZs0oE9nzSgjgJdSUBvcqWy0zMuhg',
            'GSIDNqXoacKY53MN': '1e18b8a6-13e5-44ad-b35f-bcf10b299db0',
            'STSID974004': '2b17c239-f30e-47e3-8f4f-b2fd36dbd12e',
            'ltkSubscriber-Footer': 'eyJsdGtDaGFubmVsIjoiZW1haWwiLCJsdGtUcmlnZ2VyIjoibG9hZCJ9',
            'ltkpopup-session-depth': '3-4',
            'cookie': '65e1479d-eceb-43d4-bb08-426ef7c3ac1d',
            'cookie_cst': 'zix7LPQsHA%3D%3D',
            '_li_dcdm_c': '.sears.com',
            '_lc2_fpi': 'ec742730c587--01hh09sa3h9kq3fknw05z7w35a',
            '_lc2_fpi_meta': '{%22w%22:1701891057777}',
            'cto_bundle': 'xJ3u7l9nNyUyRkcxcXh4QjQ2eXg1WmRuJTJCUmtMbHBQUjM5RFJPeCUyQlMlMkJLam5XQXRHcSUyRnlINmd2cnk3anJQeUd1SFgzbWdSMTdhSE1CQjZoa21uQWZMdDd5c3dHMVFtUDVwdWpFTzQlMkIwRDZ5T0slMkY3JTJCSVo1empMZ0NRa01EJTJCbW1DZUU5TkhwUDV4dXpiOFlVdmlGaHVQcFV2ZHZOQkElM0QlM0Q',
            'cto_bidid': 'yWwMf191d1UlMkZRRTFDZXZYVnFMTTA2N0slMkZsa29pRWRJNEtjZWhVQjhFN1lXJTJGZiUyQmdZSFVGYUV4cHdtZSUyQlYwNTlURTBZZjN2RzhvRDNBUnpaNjh6cEI5N0tXVWN3WVpDMlAyRU1hblJMQkwyVnFaVFUlM0Q',
            '__gads': 'ID=eb582ec3cf9ceeab:T=1701891057:RT=1702069798:S=ALNI_MZjz9whHNGrnpwFxuC45MsXmzVmRA',
            '__gpi': 'UID=00000d0c8e95e515:T=1701891057:RT=1702069798:S=ALNI_MZkjoDu_9-GlN3Ff6eZETKf08vfgQ',
            '__qca': 'P0-694235137-1701891057911',
            '_li_ss': 'ChMKBgjdARDVFgoJCP____8HEN8W',
            '_li_ss_meta': '{%22w%22:1702069816848%2C%22e%22:1704661816848}',
            '_pbjs_userid_consent_data': '3524755945110770',
            'cto_dna_bundle': 'qaj5S19aM1hNZjdNMDYxamYlMkZRY3RaaGt1RSUyQno5SU1PQ1dBSWR3Tk9ZV0tvM0t0clZXdlZuRUhPJTJCd01LeGswbHZmblNQSjA1a2s2eVZuQURHQ1laalZpNlNhQSUzRCUzRA',
            '_uetvid': 'f6de84b0946d11ee8db60d10473051ce',
            '__cf_bm': 'GhNo2_8S28s6arr8y385DhvHCmf17KNfAqsqb6Oulww-1702069806-1-AashSsk79bgVIUwH2nLi3ZBoMdBp2x/A5pgX+Qhk8X+ZZQbxmLLv0diFHZayPDOfSBG1tE6bRWaIxYxXLLmNS88oXWpLFO8mvD/e+cyefPX4',
            '_gid': 'GA1.2.1155879881.1702069810',
            'ftr_blst_1h': '1702069810409',
            'zipCode': '10101',
            'city': 'New York',
            'state': 'NY',
        }
        return cookies

    @staticmethod
    def get_headers():
        """Get headers for Sears API requests."""
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
            'Content-Type': 'application/json',
            'Authorization': 'SEARS',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }
        return headers

    @staticmethod
    def request_delay():
        """Delay Generation"""
        delay_seconds = random.randint(5, 12)
        time.sleep(delay_seconds)

    def get_response_from_api(self):
        """Get a response from Sears API."""
        # self.request_delay()
        product_api_link = self.get_api_link()
        cookies = self.get_cookies()
        headers = self.get_headers()
        response = requests.get(url=product_api_link,
                                cookies=cookies, headers=headers)
        data = response.json()
        return data

    def get_product_informations(self):
        """Get information about the product through the Sears API."""
        base_url = 'https://www.sears.com'
        data = self.get_response_from_api()
        product_information = {
            'name': data['productDetail']['softhardProductdetails'][0]['descriptionName'] or 'None',
            'brand': data['productDetail']['softhardProductdetails'][0]['brandName'] or 'None',
            'product_id': data['productDetail']['softhardProductdetails'][0]['identity']['sSin'] or 'None',
            'image': data['productDetail']['softhardProductdetails'][0]['mainImageUrl'] or 'None',
            'price': data['productDetail']['softhardProductdetails'][0]['salePrice'] or 'None',
            # 'price': data['productDetail']['softhardProductdetails'][0]['price']['finalPriceDisplay'] or 'None',
            'seo_url': f"{base_url}{data['productDetail']['softhardProductdetails'][0]['seoUrl']}" or 'None',
            'user_manual': data['productDetail']['softhardProductdetails'][0]['userManual'] or 'None' or 'None',
            'pre_description': data['productDetail']['softhardProductdetails'][0]['topDescription'] or 'None',
            'short_description': data['productDetail']['softhardProductdetails'][0]['shortDescription'] or 'None',
            'long_description': data['productDetail']['softhardProductdetails'][0]['longDescription'] or 'None',
            'seller': data['productDetail']['softhardProductdetails'][0]['defaultSeller']['soldBy'] or 'None',
            'parent_category': data['productDetail']['softhardProductdetails'][0]['hierarchies']['specificHierarchy'][-1]['name'] or 'None',
            'parent_category_url': f"{base_url}{data['productDetail']['softhardProductdetails'][0]['hierarchies']['specificHierarchy'][-1]['seoURL'] or 'None'}",
        }
        return product_information
