import scrapy

class NewsSpider(scrapy.Spider):
    name = "News"
    start_urls = ['https://www.reuters.com/world/']

    def parse(self, response):
        divs = response.xpath("//div[@class='StoryCollection__story___3EY8PG']")
        for div in divs:
            yield {
                'Title': div.xpath(".//h6//text()").extract(),
                'Links': div.xpath(".//a/@href").extract()

            }


