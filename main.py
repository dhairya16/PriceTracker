import requests
from bs4 import BeautifulSoup
import lxml
import re

# url = "https://www.amazon.in/Noise-Bluetooth-Headphones-Cancellation-Playback/dp/B08MB13KPM/?_encoding=UTF8&pd_rd_w=YONfT&pf_rd_p=9422ca62-08ac-429b-9d8e-f374c77b6db8&pf_rd_r=R6ZJ0G7K7B3AC1KYTH8K&pd_rd_r=786005f8-822f-4f7f-aa59-1a34e9a8aa3f&pd_rd_wg=A0DIi&ref_=pd_gw_ci_mcx_mr_hp_atf_m"
# url = "https://www.amazon.in/Rockerz-370-Headphone-Bluetooth-Lightweight/dp/B0856HNMR7/ref=sr_1_5?dchild=1&keywords=headphones&qid=1624125990&sr=8-5"
url = "https://www.amazon.in/Fire-Boltt-Bluetooth-Headphones-Lightweight-Assistance/dp/B0814GJNKG/ref=sr_1_1_sspa?dchild=1&keywords=headphones&qid=1624457545&smid=A14CZOWI0VEHLG&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzUzdJVkY0SlNLQks5JmVuY3J5cHRlZElkPUEwNzE4Nzg3MjNUSUVMV1c1OFg0MiZlbmNyeXB0ZWRBZElkPUEwMzc0MzEwMVpLM1c0MzRKNDlRUCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
# url = "https://www.amazon.in/Boat-BassHeads-900-Wired-Headphone/dp/B074ZF7PVZ/ref=sr_1_3?dchild=1&keywords=headphones&qid=1624457545&sr=8-3"

# headers = {
# 	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36",
# 	"Accept-Language": "en",
# }

# r = requests.get(url, headers = headers)

# soup = BeautifulSoup(r.text, "lxml")
# # print(soup.prettify())

# name = soup.select_one(selector = "#productTitle").getText().strip()
# # print(name)

# price = soup.select_one(selector = "#priceblock_ourprice").getText()
# price = float(price[2:])
# # print(price)

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
		price = 0
	
	price = price[2:]
	price = re.sub('[,]', '', price)
	price = float(price);

	return name, price

name, price = get_link_data(url)
print(price)