import scrapy
from articles.items import ArticlesItem


class MydailyjuiceSpider(scrapy.Spider):
    name = "mydailyjuice"
    allowed_domains = ["mydailyjuice.my"]
    start_urls = ["https://mydailyjuice.my/"]

    def parse(self, response):
        for article in response.css("div.dt-col-sm-6"):
            item = ArticlesItem()
            item["title"] = article.css("h6 > a::text").get()
            item["url"] = article.css("h6 > a::attr(href)").get()
            item["author"] = article.css("li:nth-child(1) > a > img::attr(alt)").get()

            article_url = item["url"]
            self.logger.info("Extracted article: %s, URL: %s", item["title"], article_url)
            if article_url:
                response.follow(url=article_url, callback=self.parse_article, meta={"item": item})

        next_page = response.css("div.nav-links > a.next.page-numbers::attr(href)").get()
        if next_page:
            next_page_url = response.urljoin(next_page)
            self.logger.info(
                f"Navigating to next page with URL {next_page_url}."
            )
            yield scrapy.Request(url=next_page_url, callback=self.parse)#, errback=self.log_error


    def parse_article(self, response):
        item = response.meta["item"]
        item["body"] = response.css('div[class="clearfix"] > p::text, div[class="clearfix"] > a::attr(href)').getall()
        item["tag"] = response.css('div.post-header > ul > li:nth-child(2) > a[rel="category tag"]::text').getall()
        item["date"] = response.css("div.post-header > ul > li:nth-child(3)::text").get()
        
        yield item
