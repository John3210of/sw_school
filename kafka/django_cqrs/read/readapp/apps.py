from django.apps import AppConfig
import pymysql
from pymongo import MongoClient
from datetime import datetime,date

class ReadappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'readapp'

    def ready(self):
        # 서버가 시작하자마자 해야할 일을 오버라이딩해서 쓴다.
        # 이미 유지되던 기존 서버의 데이터를 mongodb로 옮기는 데이터 동기화 작업은 여기서 하는것이 좋다.
        print("initailize")
        con = pymysql.connect(host='127.0.0.1',
                              port=3306,
                              user='root',
                              passwd='1q2w3e4r',
                              db='cqrs',
                              charset='utf8',
                              cursorclass=pymysql.cursors.DictCursor
                              )
        # conn = MongoClient('mongodb://%s%s@127.0.0.1')
        conn = MongoClient()
        db = conn.cqrs
        collect = db.books
        collect.delete_many({})
        
        cursor = con.cursor()
        cursor.execute('select * from writeapp_book')
        docs = cursor.fetchall()
        # MongoDB에 데이터를 한 번에 삽입
        
        for doc in docs:
            if isinstance(doc.get('published_date'), date):
                doc['published_date'] = datetime.combine(doc['published_date'], datetime.min.time())
        if docs:
            collect.insert_many(docs)
            print(f"{len(docs)}개의 데이터가 MongoDB에 삽입되었습니다.")
        else:
            print("삽입할 데이터가 없습니다.")
        cursor.close()
        con.close()