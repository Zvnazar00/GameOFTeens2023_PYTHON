import requests
from bs4 import BeautifulSoup as BS

r = requests.get("https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/")
html = BS(r.content, 'html.parser')

# for el in html.select((".MuiGrid-root MuiGrid-container css-2z6xcl" > . )):
for el in html.select(".MuiGrid-root MuiGrid-item MuiGrid-grid-xs-3 css-4xkoi8"):
    print(el)
