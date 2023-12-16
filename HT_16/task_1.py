"""
HT #16
 Автоматизувати процес замовлення робота за допомогою Selenium
 1. Отримайте та прочитайте дані з "https://robotsparebinindustries.com/orders.csv".
    Увага! Файл має бути прочитаний з сервера кожного разу при запускі скрипта,
    не зберігайте файл локально.
 2. Зайдіть на сайт "https://robotsparebinindustries.com/"
 3. Перейдіть у вкладку "Order your robot"
 4. Для кожного замовлення з файлу реалізуйте наступне:
     - Закрийте pop-up, якщо він з'явився. Підказка: не кожна кнопка його закриває.
     - Оберіть/заповніть відповідні поля для замовлення
     - Натисніть кнопку Preview та збережіть зображення отриманого робота.
       Увага! Зберігати треба тільки зображення робота, а не всієї сторінки сайту.
     - Натисніть кнопку Order та збережіть номер чеку. Увага! Інколи сервер тупить і
       видає помилку, але повторне натискання кнопки частіше всього вирішує проблему.
       Дослідіть цей кейс.
     - Переіменуйте отримане зображення у формат <номер чеку>_robot (напр. 123456_robot.jpg).
       Покладіть зображення в директорію output (яка має створюватися/очищатися під час
       запуску скрипта).
     - Замовте наступного робота (шляхом натискання відповідної кнопки)
 
 ** Додаткове завдання (необов'язково)
     - Окрім збереження номеру чеку отримайте також HTML-код всього чеку
     - Збережіть отриманий код в PDF файл
     - Додайте до цього файлу отримане зображення робота (бажано на одній сторінці,
       але не принципово)
     - Збережіть отриманий PDF файл у форматі <номер чеку>_robot в директорію output.
       Окремо зображення робота зберігати не потрібно. Тобто замість зображень у вас
       будуть pdf файли які містять зображення з чеком.
"""
import csv
import io
from pathlib import Path
import requests
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class OrderRobots:
    """Class for interacting with a website to order robots."""
    def __init__(self, market_url, orders_url, save_dir):
        """
        Initialize the OrderRobots instance.
         - market_url: The URL of the robot market.
         - orders_url: The URL to fetch orders in CSV format.
         - save_dir: The directory to save output files.
        """
        self.market_url = market_url
        self.orders_url = orders_url
        self.save_dir = save_dir

    def get_orders_info(self):
        """Fetch order information from the CSV URL."""
        orders_url = self.orders_url
        response = requests.get(orders_url, timeout=10)
        response.raise_for_status()
        text_csv = response.text
        csv_file = io.StringIO(text_csv)
        order_info = []
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            order_info.append({
                'order_number': row['Order number'],
                'head': row['Head'],
                'body': row['Body'],
                'legs': row['Legs'],
                'address': row['Address'],
            })
        return order_info

    @staticmethod
    def set_drive_options():
        """Set Chrome driver options."""
        options = Options()
        options.add_experimental_option("detach", True)
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_experimental_option(
            'prefs', 
            {'profile.default_content_setting_values.notifications': 2,
             'profile.default_content_settings.popups': 0})
        DEFAULT_OPTIONS = [
            '--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            '--no-sandbox',
            '--disable-application-cache',
            '--disable-web-security',
            '--allow-running-insecure-content',
            '--hide-scrollbars',
            '--disable-infobars',
            '--disable-notifications',
            '--disable-dev-shm-usage',
            '--disable-gpu',
            '--disable-setuid-sandbox',
            '--start-maximized',]
        for option in DEFAULT_OPTIONS:
            options.add_argument(option)
        return options

    @property
    def get_driver(self):
        """Get a configured instance of the Chrome WebDriver."""
        options = self.set_drive_options()
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        return driver

    def clear_save_dir(self):    
        """Clear save directory"""
        try:
            for item in self.save_dir.iterdir():
                if item.is_file() or item.is_symlink():
                    item.unlink()
                elif item.is_dir():
                    item.rmdir()
        except Exception as e:
            return f"An error occurred: {e}"

    @staticmethod
    def wait_css_selector(driver, css_selector: str):
        """Wait for an element identified by CSS selector"""
        elem_wait = wait.WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
        return elem_wait

    @staticmethod
    def wait_tag_name(driver, tag_name: str):
        """Wait for an element identified by tag name."""
        elem_wait = wait.WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, tag_name)))
        return elem_wait

    def open_start_page(self, driver, url_page):
        """Open the start page of the robot market."""
        driver.get(url_page)
        home_page_tag_name = 'html'
        home_page = self.wait_tag_name(driver=driver, tag_name=home_page_tag_name)

    def find_order_menu(self, driver):
        """Find and click the order menu button."""
        order_menu_css_selector = "a[href='#/robot-order']"
        robot_order_button = self.wait_css_selector(driver=driver, css_selector=order_menu_css_selector)
        robot_order_button.click()

    def close_pop_up(self, driver):
        """Close the pop-up window."""
        pop_up_css_selector = '.alert-buttons'
        close_css_selector = '.btn-danger'
        pop_up_window = self.wait_css_selector(driver=driver, css_selector=pop_up_css_selector)
        close_pop_up = self.wait_css_selector(driver=pop_up_window, css_selector=close_css_selector)
        close_pop_up.click()

    def put_data_in_form(self, driver, order_data):
        """Enter order data into the form."""
        order_form_tag_name = 'form'
        order_form = self.wait_tag_name(driver=driver, tag_name=order_form_tag_name)

        # Looking for the "HEAD section" in the form and enter the value
        head_value = order_data['head']
        head_css_selector = '#head'
        head_select_options = self.wait_css_selector(driver=order_form, css_selector=head_css_selector)
        select_collect = Select(head_select_options)
        select_collect.select_by_value(head_value)

        # Looking for the "BODY section" in the form and enter the value
        body_value = order_data['body']
        body_css_selector = f'input[name="body"][value="{body_value}"]'
        body_select_button = self.wait_css_selector(driver=order_form, css_selector=body_css_selector)
        body_select_button.click()

        # Looking for the "LEGS section" in the form and enter the value
        legs_value = order_data['legs']
        legs_css_selector = 'input[placeholder="Enter the part number for the legs"]'
        legs_input = self.wait_css_selector(driver=order_form, css_selector=legs_css_selector)
        legs_input.clear()
        legs_input.send_keys(legs_value)

        # Looking for the "ADDRESS section" in the form and enter the value
        address_value = order_data['address']
        address_css_selector = 'input[placeholder="Shipping address"]'
        address_input = self.wait_css_selector(driver=driver, css_selector=address_css_selector)
        address_input.clear()
        address_input.send_keys(address_value)

    def press_submit_button(self, driver):
        """Click the order submit button."""   
        order_form_tag_name = 'form'
        submit_form_css_selector = '#order'
        order_form = self.wait_tag_name(driver=driver, tag_name=order_form_tag_name)
        submit_form = self.wait_css_selector(driver=order_form, css_selector=submit_form_css_selector)
        submit_form.click()

    def search_error(self, driver):
        """Search for and handle error messages."""
        error_search_run = True
        while error_search_run:
            try:
                home_page_tag_name = 'html'
                allert_msg_css_selector = '.alert-danger'
                home_page = self.wait_tag_name(driver=driver, tag_name=home_page_tag_name)
                allert_msg = driver.find_element(By.CSS_SELECTOR, allert_msg_css_selector)
            except NoSuchElementException:
                error_search_run = False
            else:
                self.press_submit_button(driver)

    def get_order_number(self, driver):
        """Get the order number from the order completion page."""
        order_completion_css_selector = '#order-completion'
        order_inf_css_selector = '.badge-success'
        order_completion = self.wait_css_selector(driver=driver, css_selector=order_completion_css_selector)
        order_information = self.wait_css_selector(driver=order_completion, css_selector=order_inf_css_selector).text
        order_number = order_information.rsplit('-')[-1]
        return order_number

    def save_pdf_order(self, driver, order_number):
        """Save the order details as a PDF file."""
        # Get img
        robot_image_css_selector = '#robot-preview-image'
        receipt_image_css_selector = '#receipt'
        receipt_image = self.wait_css_selector(driver, css_selector=receipt_image_css_selector).screenshot_as_png
        robot_image = self.wait_css_selector(driver, css_selector=robot_image_css_selector).screenshot_as_png

        # Save img
        img_1 = Image.open(io.BytesIO(receipt_image))
        img_2 = Image.open(io.BytesIO(robot_image))
        images = [img_1, img_2]
        order_number_pref = order_number + '_robot.pdf'
        save_path = self.save_dir / order_number_pref
        images[0].save(save_path, save_all=True, append_images=images[1:])

    def order_new_robot(self, driver):
        """Order another robot by clicking the corresponding button on the order completion page."""
        order_receipt_css_selector = '#order-completion'
        submit_form_css_selector = '#order-another'
        order_receipt = self.wait_css_selector(driver, css_selector=order_receipt_css_selector)
        submit_form = self.wait_css_selector(order_receipt, css_selector=submit_form_css_selector)
        submit_form.click()

    def main(self):
        """Main method for mange the entire robots ordering process."""
        try:
            driver = self.get_driver
            url_page = self.market_url
            orders = self.get_orders_info()
            self.clear_save_dir()
            self.open_start_page(driver, url_page=url_page)
            self.find_order_menu(driver)
            self.close_pop_up(driver)
            for order in orders:
                self.put_data_in_form(driver, order)
                self.press_submit_button(driver)
                self.search_error(driver)
                self.save_pdf_order(driver, order_number=self.get_order_number(driver))
                self.order_new_robot(driver)
                self.close_pop_up(driver)
        except Exception as text_error:
            return f"Error: {text_error}"
        finally:
            driver.quit()


if __name__ == '__main__':
    SAVE_DIR_PATH = Path(__file__).resolve().parent / 'output'
    get_order_robots = OrderRobots(
        market_url = 'https://robotsparebinindustries.com',
        orders_url = 'https://robotsparebinindustries.com/orders.csv',
        save_dir = SAVE_DIR_PATH)
    get_order_robots.main()
