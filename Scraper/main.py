import requests as r
from bs4 import BeautifulSoup
import pandas as pd
import csv

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

ft_url = "https://www.some-website"
fl_req1 = r.get(ft_url)
status1 = fl_req1.status_code
if status1 == 200:
    print(f"Connected to link, code: {status1}")
else:
    print(f"Unsuccessful connection, code: {status1}")

soup = BeautifulSoup(fl_req1.text, 'html.parser')
products = soup.find_all('div',class_='ReleaseProduct-Container')
product_list = []
for product in products:
    product_name = product.find('span',class_="ProductName-primary").text
    product_price = product.find('span',class_="ProductPrice").text
    product_price = product_price.replace('$',"").strip()
    product_release_date = product.find('span',class_="ProductReleaseDate").text
    product_release_date = product_release_date.replace("-","").replace("Launch","").replace("date","").replace(":","").strip()
    product_id_link = product.find('a')['href']
    product_link = ft_url + product_id_link
    product_list.append({'name':product_name,'price':product_price,'realase date':product_release_date,'link':product_link})

df = pd.DataFrame(product_list)
df.to_csv("somefile.csv", index=False)


# finding information for certain shoe from csv
shoe = "Jordan Retro 1 High OG"

with open('footlocker_scape.csv', 'rt') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        for field in row:
            if field == shoe:
                new_link = row[3]
            else:
                pass

