from scrapy import Spider

class MySpider(Spider):
    ...
    metadata = {
        "title": "My Template",
        "description": "Description of my template.",
        "template": True,
    }