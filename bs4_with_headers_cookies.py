import requests
from bs4 import BeautifulSoup
# import lxml
import re
# import os
# import smtplib
import datetime
import json

JSON_FILE = "amazon_google_pixel_5g.json"
AMAZON_URL = "https://www.amazon.com/Google-Pixel-5G-Factory-Unlocked/dp/B09DV93S9K/ref=sr_1_4?" \
             "keywords=google+pixel&qid=1645364495&s=electronics&sprefix=goo%2Celectronics-intl-ship%2C188&sr=1-4"
my_headers = {
    "Accept-Language": "sk,cs;q=0.8,en;q=0.6,en-US;q=0.4,pl;q=0.2",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/98.0.4758.102 Safari/537.36",
    # "cookie": "i18n-prefs=EUR",
}
my_cookies = {
    "i18n-prefs": "EUR",
    "sp-cdn": "L5Z9:SK",
}

response = requests.get(url=AMAZON_URL, headers=my_headers, cookies=my_cookies)
response.raise_for_status()
amazon_page = response.text
soup = BeautifulSoup(amazon_page, "html.parser")

# print(soup.prettify())
AMAZON_PRICE_LIMIT = 55  # real price 53 - 54 USD
amazon_product_name = soup.select_one("span#productTitle").getText().strip()
print(amazon_product_name)
amazon_product_price = soup.select_one(
    "div#corePrice_desktop span.apexPriceToPay span.a-offscreen"
).getText()
print(type(amazon_product_price), " / ", amazon_product_price)
amazon_prod_pr_str = re.sub(r"[^\d,.]", '', amazon_product_price)
print(amazon_prod_pr_str)
amazon_product_price_float = float(amazon_prod_pr_str.replace(",", "."))
print(amazon_product_price_float)
print("...")

record_datetime = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
data_dict = {
    "product_name": amazon_product_name,
    "product_link": AMAZON_URL,
    "min_price": "",
    "price_history": [(str(record_datetime), amazon_product_price_float)],
}

try:
    with open(JSON_FILE, mode="r") as file:
        # Reading all old data from json file, if exists
        data = json.load(file)
        if amazon_product_price_float < data['min_price']:
            data['min_price'] = amazon_product_price_float
        data['price_history'].append(data_dict['price_history'][0])
        # print("data: ", data)
except FileNotFoundError:
    # print("File not found.")
    with open(JSON_FILE, mode="w") as file:
        data_dict['min_price'] = amazon_product_price_float
        json.dump(data_dict, file, indent=4)
else:
    with open(JSON_FILE, mode="w") as file:
        json.dump(data, file, indent=4)
