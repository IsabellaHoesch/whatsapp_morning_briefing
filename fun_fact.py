import requests
from bs4 import BeautifulSoup
import json

def gather_funfact(url_funf="https://www.xn--unntzes-wissen-isb.de/site/unnuetzes-Wissen-des-Tages.html"):
    response = requests.get(url_funf)
    soup = BeautifulSoup(response.text, "html.parser")
    funf = str("Unnützes Wissen des Tages:\n\n"+ soup.find_all("ul")[3].contents[1].next)
    return funf