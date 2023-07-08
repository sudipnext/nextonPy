import scrapy


class GyapuspiderSpider(scrapy.Spider):
    name = "gyapuspider"
    allowed_domains = ["www.gyapu.com"]
    start_urls = ["https://www.gyapu.com/category/consumer-electronics"]

    def parse(self, response):
        pass
