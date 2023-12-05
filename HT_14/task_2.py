"""
2.
Створіть програму для отримання курсу валют за певний період. 
- отримати від користувача дату (це може бути як один день так і
інтервал - початкова і кінцева дати, продумайте механізм реалізації) і назву валюти
- вивести курс по відношенню до гривні на момент вказаної дати (або за кожен
  день у вказаному інтервалі)
- не забудьте перевірку на валідність введених даних
"""
from datetime import datetime, timedelta
import json
import requests


class FindExchangeRatesByDate:
    """
    A class for finding exchange rates by date using a specified API.

    Attributes:
    - api_domain (str): The domain of the API.
    - api_url (str): The URL of the API.

    Methods:
    - __init__(self, api_domain, api_url): Constructor method to initialize the class.
    - get_calendar_date_from_user(user_data: str) -> tuple: Static method to parse user input into a valid date.
    - display_menu(): Static method to display the main menu.
    - display_menu_currency(): Static method to display the currency selection menu.
    - display_date_title(): Static method to display the title for entering a single date.
    - display_first_date_title(): Static method to display the title for entering the first date in a range.
    - display_second_date_title(): Static method to display the title for entering the second date in a range.
    - get_user_choice_currency_list(user_choice: str): Static method to map user input to a currency code.
    - get_user_currency(self): Method to get user input for selecting a currency.
    - get_user_date(self): Method to get user input for a single date.
    - create_date_range(user_start_date, user_end_date): Static method to create a date range from start to end.
    - get_data_from_json(self, calendar_date: str) -> tuple: Method to retrieve data from the API for a specific date.
    - get_pars_data(self, user_currency: str, user_date): Method to parse data obtained from the API.
    - get_display_pars_result(self, user_currency: str, user_date): Method to format and display parsed results.
    - handle_menu_choice(self, choice): Method to handle user menu choices.
    - run(self): Method to run the main program loop.
    """
    def __init__(self, api_domain, api_url):
        """
        Constructor method to initialize the FindExchangeRatesByDate class.
        """    
        self.api_domain = api_domain
        self.api_url = api_url

    @staticmethod
    def get_calendar_date_from_user(user_data: str):
        """
        Static method to parse user input into a valid date.
        """
        try:
            date_obj = datetime.strptime(user_data, '%d/%m/%Y').date()
        except Exception as text_error:
            return False, text_error
        else:
            format_date = date_obj.strftime("%d.%m.%Y")
            return True, format_date

    @staticmethod
    def display_menu():
        """
        Static method to display the main menu.
        """
        menu_elements = [
            '\n----------------------------------------\n',
             '|             Welcome to               |\n',
             '|   "UAH archive of exchange rates"    |\n',
             '----------------------------------------\n',
             'Please select your action:\n\n',
             '[1] Find exchange rates for [one day]\n',
             '[2] Find exchange rates for [range of days]\n\n',
             '[0] Exit program']

        return "".join(menu_elements)

    @staticmethod
    def display_menu_currency():
        """
        Static method to display the currency selection menu.
        """
        menu_elements = [
             '\n--------------------------------------\n',
             '| Please select currency:            |\n',
             '--------------------------------------\n',
             '[1] USD\n',
             '[2] EUR\n',
             '[3] CHF\n',
             '[4] GBP\n',
             '[5] PLZ\n',
             '[6] SEK\n',
             '[7] XAU\n',
             '[8] CAD\n\n',
             '[0] Exit program']
        return "".join(menu_elements)

    @staticmethod
    def display_date_title():
        """
        Static method to display the title for entering a single date.
        """
        title_elements = ['\n--------------------------------------\n',
                          '| Please enter the date:             |\n',
                          '--------------------------------------',]
        return "".join(title_elements)

    @staticmethod
    def display_first_date_title():
        """
        Static method to display the title for entering the first date in a range.
        """
        title_elements = ['\n--------------------------------------\n',
                          '| Please enter the first date:       |\n',
                          '--------------------------------------',]
        return "".join(title_elements)

    @staticmethod
    def display_second_date_title():
        """
        Static method to map user input to a currency code.
        """
        title_elements = ['\n--------------------------------------\n',
                          '| Please enter the srcond date:     |\n',
                          '--------------------------------------',]
        return "".join(title_elements)

    @staticmethod
    def get_user_choice_currency_list(user_choice: str):
        """
        Static method to map user input to a currency code.
        """
        currency_code = {'1': 'USD',
                         '2': 'EUR',
                         '3': 'CHF',
                         '4': 'GBP',
                         '5': 'PLZ',
                         '6': 'SEK',
                         '7': 'XAU',
                         '8': 'CAD'}
        return currency_code.get(user_choice, False)

    def get_user_currency(self):
        """
        Method to get user input for selecting a currency.
        """
        print(self.display_menu_currency())
        user_currency_choice = input('Please enter a currency code:  ')
        user_currency = self.get_user_choice_currency_list(user_choice=user_currency_choice)
        if user_currency is False:
            return user_currency
        return user_currency

    def get_user_date(self):
        """
        Method to get user input for a single date.
        """
        user_data = input('Please enter a date (dd/mm/yyyy): ')
        check_date = self.get_calendar_date_from_user(user_data=user_data)
        return check_date

    @staticmethod
    def create_date_range(user_start_date, user_end_date):
        """
        Static method to create a date range from start to end.
        """
        user_start_date = datetime.strptime(user_start_date, "%d.%m.%Y")
        user_end_date = datetime.strptime(user_end_date, "%d.%m.%Y")

        if user_start_date > user_end_date:
            return False, "Error: The second date must be no less than the first."

        date_range = [user_start_date + timedelta(days=x) for x in range((user_end_date - user_start_date).days + 1)]
        date_strings = [date.strftime("%d.%m.%Y") for date in date_range]

        return True, date_strings

    def get_data_from_json(self, calendar_date: str) -> tuple:
        """
        Method to retrieve data from the API for a specific date.
        """
        try:
            response = requests.get(self.api_url, params={'date': calendar_date})
            response.raise_for_status()
            headers = response.headers

            content_type = headers.get('Content-Type', '').lower()
            if 'application/json' not in content_type:
                return False, "'Content-Type' is not 'application/json'"

            data = response.json()
        except requests.exceptions.HTTPError as http_error:
            return False, f"HTTP error: {http_error}"
        except json.JSONDecodeError as json_error:
            return False, f"Response is not a valid JSON: {json_error}"
        except Exception as error:
            return False, f"An unexpected error occurred: {error}"
        else:
            return True, data

    def get_pars_data(self, user_currency: str, user_date):
        """
        Method to parse data obtained from the API.
        """
        info_from_json_api = self.get_data_from_json(calendar_date=user_date)

        if info_from_json_api[0] is True:
            date_exchange_rates = info_from_json_api[1]['date']
        else:
            return f"Error: {info_from_json_api[1]}"
     
        collection_exchange_rates = list()
        if info_from_json_api[1]['exchangeRate'] == []:
            collection_exchange_rates.append({'date': date_exchange_rates,
                                                'baseCurrency': 'UAH',
                                                'currency': user_currency,
                                                'purchaseRateNB': '(no data found)',
                                                'saleRateNB': '(no data found)',
                                                'saleRate': '(no data found)',
                                                'purchaseRate': '(no data found)'})
            return collection_exchange_rates

        for item in info_from_json_api[1]['exchangeRate']:    
            if item['currency'] == user_currency:
                collection_exchange_rates.append({'date': date_exchange_rates,
                                                  'baseCurrency': item.get('baseCurrency'),
                                                  'currency': item.get('currency'),
                                                  'purchaseRateNB': item.get('purchaseRateNB'),
                                                  'saleRateNB': item.get('saleRateNB'),
                                                  'saleRate': item.get('saleRate'),
                                                  'purchaseRate': item.get('purchaseRate')})
        return collection_exchange_rates

    def get_display_pars_result(self, user_currency: str, user_date):
        """
        Method to format and display parsed results.
        """
        user_date_collection = list()

        if isinstance(user_date, list):
            user_date_collection = user_date
        else:
            user_date_collection.append(user_date)
        
        result_collection = list()
        for date in user_date_collection:
            result_collection.append(self.get_pars_data(user_currency=user_currency, user_date=date))
        
        display_resault = list()
        display_resault.append('\n---------------------------------------------------\n')
        display_resault.append('|           Your exchange rate results            |\n')
        display_resault.append('---------------------------------------------------\n')
        
        for i in result_collection:
            date = f"Date: {i[0]['date']}"
            currency_pair = f"{i[0]['baseCurrency']}/{i[0]['currency']}"
            buy = f"Buy: {i[0]['purchaseRateNB'] if i[0]['purchaseRate'] is None else i[0]['purchaseRate']}"
            sell = f"Sell: {i[0]['saleRateNB'] if i[0]['saleRate'] is None else i[0]['saleRate']}"

            display_resault.append(f"{date}; {currency_pair}; {buy}; {sell}\n")
        return "".join(display_resault)

    def handle_menu_choice(self, choice):
        """
        Method to handle user menu choices.
        """
        # [1] Find exchange rates for [one day]
        if choice == '1':
            user_currency = self.get_user_currency()
            if user_currency is False:
                print("\nError: The currency code is incorrect!")
                input("\nPress Enter to continue...")
                return "Reload"
            print(f"\nCurrency: '{user_currency}' - selected successfully.\n")

            print(self.display_date_title())
            user_date = self.get_user_date()
            date = user_date[1]
            if user_date[0] is False:
                print(f"Error: {user_date[1]}")
                input("\nPress Enter to continue...")
                return "Reload"
            
            print(self.get_display_pars_result(user_currency=user_currency, user_date=date))
            input("\nPress Enter to continue...")

        # [2] Find exchange rates for [range of days]
        if choice == '2':
            user_currency = self.get_user_currency()
            if user_currency is False:
                print("\nError: The currency code is incorrect!")
                input("\nPress Enter to continue...")
                return "Reload"
            print(f"\nCurrency: '{user_currency}' - selected successfully.\n")

            print(self.display_first_date_title())
            user_start_date = self.get_user_date()
            start_date = user_start_date[1]
            if user_start_date[0] is False:
                print(f"Error: {user_start_date[1]}")
                input("\nPress Enter to continue...")
                return "Reload"

            print(self.display_second_date_title())
            user_end_date = self.get_user_date()
            print("(!) Processing your request may take a long time!")
            end_date = user_end_date[1]
            if user_end_date[0] is False:
                print(f"Error: {user_end_date[1]}")
                input("\nPress Enter to continue...")
                return "Reload"
            
            date_range_result = self.create_date_range(user_start_date=start_date, user_end_date=end_date)[1]
            print(self.get_display_pars_result(user_currency=user_currency, user_date=date_range_result))
            input("\nPress Enter to continue...")
    
        # [0] Exit program
        elif choice == '0':
            print("Exit the program.")
            return False
        else:
            print("Invalid input. Please select an action from the list.")
        return True

    def run(self):
        """
        Method to run the main program loop.
        """
        while True:
            print(self.display_menu())
            user_choice = input("Your choice: ")
            if not self.handle_menu_choice(user_choice):
                break


if __name__ == "__main__":
    API_DOMAIN = 'https://api.privatbank.ua'
    API_URL = 'https://api.privatbank.ua/p24api/exchange_rates'
    exchange_rate_period = FindExchangeRatesByDate(api_domain=API_DOMAIN, api_url=API_URL)
    print(exchange_rate_period.run())
