import requests
from bs4 import BeautifulSoup

def translator(text):
    URL = "http://www.romajidesu.com/translator"
    payload = {
        "k" : f"{text}",
        "m" : "converters",
        "a" : "kanji_romaji",
    }
    r = requests.post(URL, data=payload)
    html = BeautifulSoup(r.text,"html.parser")
    result = html.select("#res_romaji > span")
    res = ""
    for x in result:
        res = res+" "+x.get_text()
    return res.rstrip()


