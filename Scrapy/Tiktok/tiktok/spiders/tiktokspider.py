import scrapy


class TiktokSpider(scrapy.Spider):
    name = "tiktokspider"
    allowed_domains = ["tiktok.com"]
    start_urls = ["https://tiktok.com/@khaby.lame"]

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(url=url, callback=self.parse)

    def parse(self, response):
        # Extract the desired data from the page using XPath or CSS selectors
        # ...

        # Scroll the page to load more content
        yield from self.scroll_page(response)

    def scroll_page(self, response):
        # Scroll the page to load more content
        # Adjust the scroll behavior as needed (e.g., scroll down multiple times or to a specific element)
        # Use JavaScript to execute the scroll action

        # Example: Scroll down the page once
        script = "window.scrollTo(0, document.body.scrollHeight);"
        self.selenium.execute_script(script)

        # Wait for the page to load after scrolling (if necessary)
        self.selenium.implicitly_wait(5)

        # Return a new request to continue parsing the scrolled page
        return SeleniumRequest(url=response.url, callback=self.parse)
