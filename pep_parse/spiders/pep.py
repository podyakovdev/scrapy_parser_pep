import scrapy

from pep_parse.items import PepParseItem
from pep_parse.utils import check_status


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        links = response.css(
            'table.pep-zero-table'
        ).css('tbody').css('a[href^="pep-"]')
        for pep_link in links:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        h1 = response.css('h1.page-title::text').get()
        table = response.css('dl.rfc2822')
        status = table.css('dt:contains("Status") + dd').css('abbr::text').get()
        data = {
            'number': int(h1.split()[1]),
            'name': h1,
            'status': check_status(status),
        }

        yield PepParseItem(data)
