import requests
from bs4 import BeautifulSoup
from pprint import pprint
# import lxml

URL = "http://dsl.sk/"

response = requests.get(URL)
response.raise_for_status()

dsl_web = response.text

soup = BeautifulSoup(dsl_web, "html.parser")

news_box_div = soup.select(selector="div#news_box a")
# pprint(news_box_div)

print(type(news_box_div), len(news_box_div))

news_list = []
for news in news_box_div:
    tag = news.get("href")
    if "#discussion" not in tag:
        temp_list = [news.getText(), f"http://dsl.sk/{news.get('href')}", news.next_sibling[2:-2]]
        news_list.append(temp_list)

pprint(news_list)
