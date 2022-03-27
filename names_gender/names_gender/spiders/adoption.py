import logging

import scrapy


class AdoptionSpider(scrapy.Spider):
    name = 'adoption'
    page_number = 2
    start_urls = ['https://adoption.com/baby-names/origin/Filipino?page=1']

    def parse(self, response):
        self.logger.setLevel(logging.INFO)
        rows = response.xpath("//tr")

        for index, row in enumerate(rows[1:], start=1):
            name = row.xpath("./td[@class='text-wrap']/text()").extract_first()

            try:
                gender = row.xpath("./td/text()").extract()[2]

            except ValueError:
                name = ""
                gender = ""

            yield {
                "name": name,
                "gender": gender
            }

            self.logger.info(f"DONE: {index} Extracting {name} and {gender}")

        next_page = f"https://adoption.com/baby-names/origin/Filipino?page={self.page_number}"

        self.logger.info(f"Following page: {self.page_number}")

        if next_page is not None and self.page_number <= 28:
            yield response.follow(next_page, callback=self.parse)

            self.page_number += 1
