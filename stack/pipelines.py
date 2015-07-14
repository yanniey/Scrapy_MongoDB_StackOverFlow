# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
# from pymongo import MongoClient
from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log

# class StackPipeline(object):
#     def process_item(self, item, spider):
#         return item


# Establish a connection to database, unpack the data, and then save it to the database
class MongoDBPipeline(object):
	def __init__(self):
		connection = pymongo.MongoClient(
				settings['MONGODB_SERVER'],
				settings['MONGODB_PORT']
			)
		db = connection[settings['MONGODB_DB']]
		self.collection = db[settings['MONGODB_COLLECTION']]

	# before adding to MongoDB, check to make sure that it's not a duplicate entry
	def process_item(self,item, spider):
		valid = True
		for data in item:
			if not data:
				raise DropItem("Missing data!")
		self.collection.update({'url':item['url']},dict(item),upsert=True)
		log.msg("Question added to MongoDB database", level = log.DEBUG, spider = spider)
		return item
