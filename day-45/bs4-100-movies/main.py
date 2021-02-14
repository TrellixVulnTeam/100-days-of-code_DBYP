from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
# movie = soup.find("div", class_="jsx-3821216435 listicle-item")
# print(movie.title.getText())

# tag = soup.find("picture", class_="jsx-4015086601")
all_anchor_tags = soup.find_all(name="picture")
print(all_anchor_tags)

# It seems not to work with BeautifulSoup..
