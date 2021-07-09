import scrapy

# XPATHS

# links = '//a[starts-with(@href, "collection") and (parent::h3|parent::h2)]/@href'

class ScrapyCIA(scrapy.Spider):
    name = 'cia'
    starts_url = [
        'https://www.cia.gov/readingroom/historical-collections'
    ]

    custom_settings: {
        'FEED_URI': 'cia.json',
        'FEED_FORMAT': 'json',
        'FEED_EXPORT_ENCODING': 'utf-8',
        'ROBOTSTXT_OBEY': True   
    }

    def parse(self, response):
        pass
        