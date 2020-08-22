# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class SpiderPipeline:
    def open_spider(self, spider):
        self.article = open('./doubanmovie.csv', 'a', encoding='utf-8')

    # 每一个item管道组件都会调用该方法，并且必须返回一个item对象实例或raise DropItem异常
    def process_item(self, item, spider):
        name = item['name']
        category = item['category']
        show_time = item['show_time']
        output = f'|{name}|\t|{category}|\t|{show_time}|\n\n'
        self.article.write(output)
        return item

    def close_spider(self, spider):
        self.article.close()