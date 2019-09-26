# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html


from scrapy.item import Item, Field

class BggdatascrapingItem(Item):
	title = Field()
	rank = Field()
	release_date = Field()
	geek_rating = Field()
	avg_rating = Field()
	num_voters = Field()
	url = Field()

