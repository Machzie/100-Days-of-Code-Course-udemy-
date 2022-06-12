# Day 45 project - 100 Movies Web Scraping

from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

titles = soup.find_all(name="h3", class_="title")
names = [f"{title.getText()}\n" for title in titles]

with open("movies.txt", "w") as file:
    file.writelines(names[::-1])
