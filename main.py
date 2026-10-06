import requests
from bs4 import BeautifulSoup
# year=input("enter the year you need to go?yyyy-mm-dd:")
url="https://appbrewery.github.io/bakeboard-hot-100/2026-04-18/"
data=requests.get(url=url).text
soup=BeautifulSoup(data,"html.parser")
# print(soup.prettify())
list_of_top_songs=soup.find_all(name="h3",class_="chart-entry__title")
index=1
for song in list_of_top_songs:
    print(f"{index}:{song.get_text()}")
    index+=1