import scrapy


class MydailyjuiceSpider(scrapy.Spider):
    name = "mydailyjuice"
    allowed_domains = ["mydailyjuice.my"]
    start_urls = ["https://mydailyjuice.my/"]

    def parse(self, response):
        pass
