from bs4 import BeautifulSoup
import requests
import lxml
import re

def get_link_data(url):
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36",
		"Accept-Language": "en",
	}

	r = requests.get(url, headers = headers)

	soup = BeautifulSoup(r.text, "lxml")
	name = soup.select_one(selector = "#productTitle").getText().strip()

	obj = soup.select_one(selector = "#priceblock_dealprice")
	if obj is None:
		obj = soup.select_one(selector = "#priceblock_ourprice")

	if obj != None:
		price = obj.getText()
	else:
		price = 0.0

	if price != 0.0:
		price = price[1:]
		price = re.sub('[,]', '', price)
		price = float(price);

	return name, price
