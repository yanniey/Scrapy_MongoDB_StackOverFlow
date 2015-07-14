# Web scraping with Scrapy and MongoDB
7/12/2015

## Part 1: Spider is named `stack`, see `stack_spider.py`

Use [Scrapy](http://scrapy.org/) to crawl the 50 latest submitted questions on [StackOverflow](https://stackoverflow.com/), output data to JSON file, validate the data entires, then import to [MongoDB](https://www.mongodb.org/) database.

## Part 2: Spider is named `stack_crawler`, see`stack_crawler.py`

Use Scrapy's [Crawlspider](http://doc.scrapy.org/en/latest/topics/spiders.html#crawlspider) to extend the scraper so that it crawls through the pagination links at the bottom of each page and scrapes the questions (question title and URL) from each page. (Translate: let's scrape > 50 questions at a time!)

Note: 
Replace deprecated `pymongo.Connection()` with `MongoClient.Connection()` according to PyMongo 3.0's update

Output JSON files in Scrapy:

```
scrapy crawl stack -o items.json -t json
scrapy crawl stack_crawler -o items3.json -t json
```