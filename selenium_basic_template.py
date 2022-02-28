from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.common.action_chains import ActionChains
# https://stackoverflow.com/questions/3401343/scroll-element-into-view-with-selenium
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
import time

my_service = Service(r'C:\Users\Radovan\Development\chromedriver_win32\chromedriver.exe')
# chrome_locale = "sk-sk"

my_capabilities = DesiredCapabilities().CHROME

my_options = Options()
my_options.add_argument('window-size=1800,1800')
# my_options.add_argument("--lang={}".format(chrome_locale))
my_options.add_argument('--user-data-dir=D:\\0media\\Pictures\\zwieratko.sk\\random_person')  # Set user data folder
# my_options.add_argument('--headless')  # headless mode
# my_options.add_argument('--disable-gpu')  # Disable GPU acceleration
# my_options.add_argument('--start-maximized')  # The browser is maximized
# my_options.add_argument('--window-size=1280x1024')  # Set browser resolution (window size)
# my_options.add_argument('log-level=3')  # Logging level
# info(default) = 0
# warning = 1
# LOG_ERROR = 2
# LOG_FATAL = 3
# my_options.add_argument('--user-agent=""')  # Set the User-Agent of the request header
# my_options.add_argument('--incognito')  # Incognito mode (incognito mode)
# my_options.add_argument('--hide-scrollbars')  # hide the scrollbars to deal with some special pages
# my_options.add_argument('--disable-javascript')  # disable javascript
# my_options.add_argument('--blink-settings=imagesEnabled=false')  # Do not load images, improve speed
# 0 - Default, 1 - Allow, 2 - Block
prefs = {
    'profile.default_content_setting_values':
    {
        'notifications': 1,
        'geolocation': 1,
    },

    'profile.managed_default_content_settings':
    {
        'geolocation': 1,
    },
}
my_options.add_experimental_option('prefs', prefs)
my_options.add_experimental_option("detach", True)
my_capabilities.update(my_options.to_capabilities())

browser = webdriver.Chrome(service=my_service, options=my_options)
time.sleep(5)
browser.get("https://zwieratko.sk")  # about:blank
print(browser.title)
time.sleep(2)
browser.refresh()

wait = WebDriverWait(browser, 10)
cookies_accept_btn_list = browser.find_elements(By.CSS_SELECTOR, "button.fc-cta-consent")
print(type(cookies_accept_btn_list), len(cookies_accept_btn_list))
if len(cookies_accept_btn_list) != 0:
    try:
        cookies_accept_btn = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "button.fc-cta-consent")))
    except TimeoutException:
        print("We spent 10s. There is no cookies accept button or it is already accepted.")
    else:
        cookies_accept_btn.click()

print("END.")
