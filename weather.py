import requests
from bs4 import BeautifulSoup
import json


def gather_weather(url_wetter="https://www.wetter.com/deutschland/muenchen/DE0006515.html"):
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
    return weather_list

