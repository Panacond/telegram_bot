from bs4 import BeautifulSoup
import requests, os

def weather_sinoptic():
    page = requests.get("https://sinoptik.ua/погода-одесса")
    soup = BeautifulSoup(page.content, 'html.parser')
    list_html = soup.select("tr.temperatureSens > td")
    list_text = [x.get_text() for x in list_html]
    if len(list_text) == 7:
        list_text = list_text[2:-1]
    else:
        list_text = list_text[2:-2]
    text = """Cегодня в Одессе:
Утро 9:00  {0}
Утро 12:00 {1}
День 15:00 {2}
День 18:00 {3}"""
    return text.format(list_text[0],list_text[1],list_text[2], list_text[3])


if __name__ == "__main__":
    print(weather_sinoptic())
