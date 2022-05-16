import scrapy
from ..items import AmazonScraperItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = ['https://www.amazon.com/s?k=dress&crid=2KM5XO18CLK73&sprefix=dress%2Caps%2C199&ref=nb_sb_noss_1']

    def parse(self, response):
        items = AmazonScraperItem()

        product_name = response.css('.a-color-base.a-text-normal').extract()
        product_image = response.css('.s-image').extract()

        items['product_name'] = product_name
        items['product_image'] = product_image

        yield items
