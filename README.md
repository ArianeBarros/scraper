# scraper
Antes:
pip install scrapy
pip install --upgrade attrs

Rodar:
scrapy runspider spider.py


This project contains 2 scrapers, 1 for brands and 1 for mercado livre. The brands one is in the folder Crawler-Brands/Crawler-Brands. After scraping the brands name, we load the data into a json file called marcas.json, which is then added to mongodb with the script myclient.py

The mercado livre is in the root, and scrapes name of the product and its URL. 
