from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from realest.spiders.sahibinden_com import SahibindenComSpider
from realest import settings


def main():
    crawler_secctings = Settings()
    crawler_secctings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_secctings)
    process.crawl(SahibindenComSpider)
    process.start()


if __name__ == "__main__":
    main()