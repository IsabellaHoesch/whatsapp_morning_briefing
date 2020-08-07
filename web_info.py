"""
3 functions that scrape websites for information on: news, weather, funfact.
- gather_headlines()
- gather_weather()
- gather_funfact()
"""

import requests
from bs4 import BeautifulSoup
import json

def gather_headlines(url_news="https://www.handelsblatt.com/ticker/"):
    """
    Scraping news from selected website
    :param url_news: url from news website
    :return: string of 10 top headlines
    """
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
    headlines_string='\n\n'.join(headlines_list)
    return headlines_string


def gather_weather(url_wetter="https://www.wetter.com/deutschland/muenchen/DE0006515.html"):
    """
    Scraping weather from selected website (chosen location: Munich, Germany)
    :param url_weather: url from weather website
    :return: string with links for weather: morning, noon, evening, night
    """
    response = requests.get(url_wetter)
    soup = BeautifulSoup(response.text, "html.parser")
    when = ["Morgens", "Mittags", "Abends", "Nachts"]
    imgs_list = []
    for link in soup.find_all("img")[-5:-1]:
        imgs_list.append(link.get("src"))
    temp_list = []
    for t in soup.find_all(attrs={"class": "beta"})[1:5]:
        temp_list.append(t.next)
    weather_list= []
    for time, img, temp in zip(when, imgs_list, temp_list):
        weather_list.append('Wetter in München %s: %s %s' % (time, temp, img))
    weather_string = '\n\n'.join(weather_list)
    return weather_string


def gather_funfact(url_funf="https://www.xn--unntzes-wissen-isb.de/site/unnuetzes-Wissen-des-Tages.html"):
    """
    Scraping funfact from selected website (language = German)
    :param url_funfact: url from funfact website
    :return: string of funfact
    """
    response = requests.get(url_funf)
    soup = BeautifulSoup(response.text, "html.parser")
    funf = str("Unnützes Wissen des Tages:\n\n"+ soup.find_all("ul")[3].contents[1].next)
    return funf


