from django.apps import AppConfig
import pymysql
from pymongo import MongoClient
from datetime import datetime,date
from kafka import KafkaConsumer
from threading import Thread
import json
class ReadappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'readapp'
    
    def ready(self):
        print("Initialize: Syncing existing data to MongoDB.")
        self._sync_data_to_mongodb()

        print("Starting Kafka Consumer...")
        #TODO: thread를 할당하는 이유에 대해 정리
        consumer_thread = Thread(target=self._start_kafka_consumer)
        consumer_thread.daemon = True  # 서버가 종료되면 스레드도 종료
        consumer_thread.start()

    def _sync_data_to_mongodb(self):
        #TODO 매번 서버를 새로 킬 때 마다, DB dump시키는 방법이 맞는 것일지? 에 대한 고민을 해봐야함
        """기존 MySQL 데이터를 MongoDB로 동기화하는 메서드."""
        con = pymysql.connect(host='127.0.0.1',
                              port=3306,
                              user='root',
                              passwd='1q2w3e4r',
                              db='cqrs',
                              charset='utf8',
                              cursorclass=pymysql.cursors.DictCursor)
        conn = MongoClient()  # MongoDB 연결
        db = conn.cqrs
        collect = db.books
        collect.delete_many({})
        cursor = con.cursor()
        cursor.execute('SELECT title, author, category, pages, price, published_date, description FROM writeapp_book')
        docs = cursor.fetchall()
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

    def _start_kafka_consumer(self):
        """Kafka Consumer를 실행하여 메시지를 MongoDB로 저장."""
        consumer = KafkaConsumer(
            'books-topic',
            bootstrap_servers='localhost:9092',
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='book-group',
            value_deserializer=lambda v: json.loads(v.decode('utf-8'))
        )
        conn = MongoClient()
        db = conn.cqrs
        collect = db.books
        print("Kafka Consumer가 메시지를 수신합니다...")
        for message in consumer:
            book_data = message.value
            print(f"Kafka 메시지 수신: {book_data}")
            if isinstance(book_data.get('published_date'), str):
                book_data['published_date'] = datetime.strptime(book_data['published_date'], "%Y-%m-%d")
            collect.insert_one(book_data)
            print("MongoDB에 데이터가 삽입되었습니다.")

    def old_ready(self):
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
        conn = MongoClient()
        db = conn.cqrs
        collect = db.books
        collect.delete_many({})
        cursor = con.cursor()
        cursor.execute('select * from writeapp_book')
        docs = cursor.fetchall()
        
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