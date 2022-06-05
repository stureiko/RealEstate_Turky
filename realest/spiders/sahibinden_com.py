import scrapy
from scrapy.http import HtmlResponse

class SahibindenComSpider(scrapy.Spider):
    name = 'sahibinden_com'
    allowed_domains = ['sahibinden.com']
    start_urls = ['https://www.sahibinden.com/satilik-daire/istanbul?a20=38470']

    def parse(self, response: HtmlResponse):
        flats = response.xpath("//table[@id='searchResultsTable']/tbody//tr[@data-id]/@href").extract()
        pass
