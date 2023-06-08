import scrapy
import json

def urls_brands():
    base_url = 'https://www.rankingthebrands.com/The-Brands-and-their-Rankings.aspx?catFilter=0&nameFilter='
    alphabet = 'ABCDEFGHIJKLMNO'
    urls = list()
    for c in alphabet:
        urls.append(base_url + c)
    return urls


def write_results(brands):
    sorted_brands = sorted(brands, key=lambda d: d['name'])
    jsonstring = json.dumps(sorted_brands, indent=2)
    output_file = open('marcas.json', 'a')
    output_file.write(jsonstring)
    output_file.close()

class BrandsSpider(scrapy.Spider):
    name = 'brands'
    start_urls = urls_brands()
    # esta sera a lista de marcas depois do agente ter feito o trabalho.
    brands = list()

    def parse(self, response):
        for e in response.css('.rankingName'):
            brand_to_write = e.css('::text').get()
            self.brands.append({'name': brand_to_write})
            #yield {'name': brand_to_write}

    def close(self, reason):
        write_results(self.brands)