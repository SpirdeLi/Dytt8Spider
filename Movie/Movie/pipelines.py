# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from Movie import settings
import pymysql.cursors
from scrapy import log

class MoviePipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host = settings.MYSQL_HOST,
            port = settings.MYSQL_PORT,
            db = settings.MYSQL_DBNAME,
            user = settings.MYSQL_USER,
            password = settings.MYSQL_PASSWD,
            charset = 'utf8',
            use_unicode=True,
        )
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        mysql_insert = ('insert into MovieInfos(Movieurl,Moviename,Moviecategory,Image,Introductions,Downloadurl,actors) VALUES ("%s","%s","%s","%s","%s","%s","%s")'%
                       (item['Movieurl'], item['Moviename'], item['Moviecategory'], item['Image'], item['Introductions'],
                        item['Downloadurl'], item['actors']))

        # self.cursor.execute(mysql_insert)
        # self.connect.commit()

        return item



