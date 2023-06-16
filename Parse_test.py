import requests
from bs4 import BeautifulSoup

url = "https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/"

response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")

tariffs = soup.find_all("div", class_="block-tarif-plan")

for tariff in tariffs:
    title = tariff.find("div", class_="tarif-plan__name").text.strip()
    description = tariff.find("div", class_="tarif-plan__desc").text.strip()
    price = tariff.find("div", class_="tarif-plan__price").text.strip()

    print("Название:", title)
    print("Описание:", description)
    print("Цена:", price)
    print("----------------------")
