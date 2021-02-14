from bs4 import BeautifulSoup
import lxml

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.a)
# print(soup.p)
# print(soup.li)

all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
    # print(tag.getText())
    # print(tag.get("href"))

heading = soup.find(name="h1", id="name")
# print(heading)

section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
# print(section_heading.get("class"))

company_url = soup.select_one(selector="p a") #narrow down
# print(company_url)

name = soup.select_one(selector="#name")
# print(name)

headings = soup.select(".heading") #ALL elements that has a class heading
print(headings)
