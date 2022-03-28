from selenium import webdriver
from selenium.webdriver.common.by import By
def translate(word, language="en"):
    if "en" == language:
        url =f"https://translate.google.com/?hl=ru&sl=en&tl=ru&text={word}&op=translate"
    else:
        url = f"https://translate.google.com/?hl=ru&sl=ru&tl=en&text={word}&op=translate"

    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(3)
    text = driver.find_element(By.CSS_SELECTOR, "span.VIiyi > span > span").text

    driver.quit()
    return text.lower()


if __name__ == '__main__':
    assert "thing" == translate("ру вещь")
    assert "слово" == translate("En word")
