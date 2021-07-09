import scrapy

class ScrapyCIA(scrapy.Spider):
    name = 'cia'

    start_urls = [
        'https://www.cia.gov/readingroom/historical-collections'
    ]
    custom_settings={
            'FEEDS':{
                'cia.json':{
                    'format': 'json',
                    'encoding': 'utf-8',
                    'indent': 4,
                    }
                    },
        }

    # XPATHS
    declassified_links = '//a[starts-with(@href, "collection") and (parent::h3|parent::h2)]/@href'
    title = '//h1[@class="documentFirstHeading"]/text()'
    body = '//div[contains(@class, "field-item")]/p[not(child::strong and child::i) and not(@class)]/text()'
    def parse(self, response):
        links = response.xpath(self.declassified_links).getall()
        
        for l in links:
            full_link = response.urljoin(l)
            yield response.follow(l, callback=self.parse_link, cb_kwargs={'url': full_link})


    def parse_link(self, response, **kwargs):
        link = kwargs['url']

        title = response.xpath(self.title).get()
        body = ''.join(response.xpath(self.body).getall())


        yield {
            'url': link,
            'title': title,
            'body': body
        }

        