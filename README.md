# Web scraping with Scrapy and MongoDB
7/12/2015

Use [Scrapy](http://scrapy.org/) to crawl the 50 latest submitted questions on [StackOverflow](https://stackoverflow.com/), output data to JSON file, validate the data entires, then import to [MongoDB](https://www.mongodb.org/) database.

Note: 
Replace deprecated `pymongo.Connection()` with `MongoClient.Connection()` according to PyMongo 3.0's update

Output JSON files in Scrapy:

```
scrapy crawl stack -o items.json -t json
```