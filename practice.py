from bs4 import BeautifulSoup
import lxml

with open('index.html', 'r') as file:
	body = file.read()

soup = BeautifulSoup(body, 'lxml')
# print(soup.prettify())

movie = soup.find('div', class_='movie')
parent = movie.find_parent('div')
print(parent.prettify())