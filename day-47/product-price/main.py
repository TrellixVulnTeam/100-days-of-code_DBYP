from bs4 import BeautifulSoup
import lxml
import requests

URL = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07WL1XBBD/ref=sr_1_1?qid=1597662463&th=1"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,la;q=0.8"
}


response = requests.get(URL, headers=header)

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

price = float(soup.find(id="priceblock_ourprice").get_text().split("$")[1])
# print(price)
