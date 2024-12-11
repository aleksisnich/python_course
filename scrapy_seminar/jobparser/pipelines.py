# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient

class JobparserPipeline:
    # def __int__(self):
    #     client = MongoClient('localhost', 27017)
    #     self.mongo_base = client.vacancies111224

    def process_item(self, item, spider):
        client = MongoClient('localhost', 27017)
        self.mongo_base = client.vacancies111224
        # item.get("salary")
        # item["min_salary"] = item.get("salary")[1]
        # item["max_salary"] = item.get("salary")[3]
        collection = self.mongo_base[spider.name]
        collection.insert_one(item)

        return item
