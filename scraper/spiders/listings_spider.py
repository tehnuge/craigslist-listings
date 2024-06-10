from pathlib import Path

import scrapy

# Run the spider with the following command: 
# scrapy crawl listings -O listings.json
# This will save the output to a file named listings.json
class ListingsSpider(scrapy.Spider):
    name = "listings"

    def start_requests(self):
        urls = [
            "https://sfbay.craigslist.org/search/rea#search=1~gallery~0~0",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        posts = response.xpath("//a[starts-with(@href, 'https')]")
        for p in posts:
            yield {
                "title": p.css("div.title::text").get(),
                "url": p.attrib["href"]
            }