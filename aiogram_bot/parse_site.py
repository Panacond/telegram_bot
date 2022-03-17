from bs4 import BeautifulSoup
import requests

def weather_sinoptic():
    page = requests.get("https://sinoptik.ua/погода-одесса")
    soup = BeautifulSoup(page.content, 'html.parser')
    list_html = soup.select("tr.temperatureSens > td")
    list_text = [x.get_text() for x in list_html]

    list_text = list_text[2:-2]
    text = """Cегодня в Одессе:
Утро 8:00  {0}
Утро 11:00 {1}
День 14:00 {2}
День 17:00 {3}"""
    return text.format(list_text[0],list_text[1],list_text[2], list_text[3])

