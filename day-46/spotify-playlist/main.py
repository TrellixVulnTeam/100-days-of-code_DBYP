from bs4 import BeautifulSoup
import requests

URL = "https://www.billboard.com/charts/hot-100/"

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# date = "2000-08-08"

response = requests.get(URL+date)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

titles = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
titles_list = [title.getText() for title in titles]
print(titles_list)