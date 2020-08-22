# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class SpiderPipeline:
    def process_item(self, item, spider):
        name = item['name']
        category = item['category']
        show_time = item['show_time']
        output = f'|{name}|\t|{category}|\t|{show_time}|\n\n'
        with open('./maoyanmovie.csv', 'a+', encoding='utf-8') as article:
            article.write(output)
        return item
