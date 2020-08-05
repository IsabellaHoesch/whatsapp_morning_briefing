#scrape news

import requests
from bs4 import BeautifulSoup
import json

def gather_headlines(url_news="https://www.handelsblatt.com/ticker/"):
    response = requests.get(url_news)
    soup = BeautifulSoup(response.text, "html.parser")
    headlines = soup.find_all(attrs={"class": "vhb-headline"})
    count = 1
    headlines_list=[]
    for headline in headlines[1:]:
        headlines_list.append('Headline %s: %s' % (count, headline.text))
        count += 1
        if count == 10:
            break
    return headlines_list


