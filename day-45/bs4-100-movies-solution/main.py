"""Save the browser rendered page locally, so that browser will save the rendered HTML version of the react templates
rather than directly downloading react based files. Not really a practical approach to web scraping. Plus there was a
lot of weirdness with the numbering when I tried this. Missing numbers, numbers out of sequence, repeated numbers,
etc etc.. """

from bs4 import BeautifulSoup

FILE = 'The 100 Greatest Movies _ Movies _ Empire.html'

with open(FILE) as html_file:
    html_date = html_file.read()

soup = BeautifulSoup(html_date, 'html.parser')

tags_list = soup.find_all(name='h3', class_='jsx-2692754980')  # See the weird class name?
movie_rankings = [(item.getText()) for item in tags_list]

file_string = ''

movies = movie_rankings[::-1]

for movie in movies:
    file_string += f'{movie}\n'

with open('movies2.txt', 'w', encoding='utf-16') as file:
    file.write(file_string)