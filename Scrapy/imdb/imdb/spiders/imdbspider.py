import scrapy
import numpy as np
import time


class ImdbspiderSpider(scrapy.Spider):
    name = "imdbspider"
    start_urls = ["https://myanimelist.net/character/1"]
    alphabets = np.arange(3000, 4000, 1)

    def start_requests(self):
        for alpha in self.alphabets:
            # time.sleep(1)
            url = f"https://myanimelist.net/character/{alpha}"
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        name_xpath ="//h2[contains(@class, 'normal_header')]/text()"
        names = response.xpath(name_xpath).getall()
        name = response.xpath(name_xpath).get()
        height_xpath = f"//h2[contains(text(), '{name}')]/following-sibling::text()[contains(., 'Height')]"
        heights = response.xpath(height_xpath).getall()
        for name, height in zip(names, heights):
            name = name.strip()
            height = height.strip()
            yield {
                'name': name,
                'height': height
            }
