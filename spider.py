import scrapy
import json
import base64
from myclient import MyDB
from myclient import Brand

def urls_brands():
    base_url = 'https://www.rankingthebrands.com/The-Brands-and-their-Rankings.aspx?catFilter=0&nameFilter='
    alphabet = 'ABCDEFGHIJKLMNO'
    urls = list()
    for c in alphabet:
        urls.append(base_url + c)
    return urls


def write_results(brands):
    sorted_brands = sorted(brands, key=lambda d: d['name'])
    jsonstring = json.dumps(sorted_brands)
    output_file = open('marcas.json', 'w')
    output_file.write(jsonstring)
    output_file.close()

class BrandsSpider(scrapy.Spider):
    name = 'brands'
    start_urls = ["https://www.mercadolivre.com.br/c/celulares-e-telefones#menu=categories"]
    # esta sera a lista de marcas depois do agente ter feito o trabalho.
    brands = list()
    db = MyDB()

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    }

    def parse(self, response):
         for e in response.css('#special'):
            brand_to_write = e.css('h3::text').get()
            img_url = e.css('img::attr(src)').get()
            self.brands.append({'name': brand_to_write, 'url': img_url})
            #yield {brand}
    
    def close(self, reason):
        write_results(self.brands)
        
