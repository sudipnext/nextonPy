import scrapy
from gajabko.items import GajabkoItem

class GajabkospiderSpider(scrapy.Spider):
    name = "gajabkospider"
    allowed_domains = ["gajabko.com"]
    start_urls = ["https://gajabko.com/product-category/electronics/"]

    def parse(self, response):
        electronics = response.css('li.has-post-thumbnail')
        for electro in electronics:
            relative_url = electro.css('a::attr(href)').get()
            yield scrapy.Request(relative_url, callback=self.parse_product_page)


        next_page = response.xpath('//ul[@class="page-numbers"]/li[last()]//a/@href').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
    
    def parse_product_page(self, response):
        product = response.css('div.entry-summary')[0]
        p_tags = p_tags = product.xpath('//div[@itemprop="description"]/p')
        description = [p_tag.xpath('.//text()').get().strip() for p_tag in p_tags]
        gajab_item = GajabkoItem()
        gajab_item['url']: response.url
        gajab_item['title']: product.css('h1.product_title::text').get()
        gajab_item['price']: product.xpath('//meta[@itemprop="price"]/@content').get()
        gajab_item['description']: description
        gajab_item['image_url']: response.css('div.images a::attr(href)').get()
        yield gajab_item
