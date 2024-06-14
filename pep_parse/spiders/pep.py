import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        pep_links = response.css(
            'section[id="numerical-index"] table.pep-zero-table tbody tr'
            )

        for link in pep_links:
            href = link.css('td:nth-child(2) a::attr(href)').get()
            number = self.extract_pep_number(href)
            yield response.follow(
                href, self.parse_pep, meta={'number': number}
                )

    def parse_pep(self, response):
        number = response.meta['number']
        name = response.css('h1.page-title::text').get()
        status = response.css('dt:contains("Status") + dd abbr::text').get()

        item = PepParseItem(number=number, name=name, status=status)
        yield item

    def extract_pep_number(self, href):
        # Пример href: 'pep-0001/'
        return href.split('-')[-1].rstrip('/')
