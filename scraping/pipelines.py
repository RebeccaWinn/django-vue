from itemadapter import ItemAdapter
import sqlite3
  
  
class ScrapyPipeline(object):
    def process_item(self, item, spider):
        item.save()
        return item
