from pymongo import MongoClient

client = MongoClient('localhost', 27018)
db = client.mydatabase
collection = db.mycollection
data = {"name": "Alice", "age": 30, "city": "New York"}
collection.insert_one(data)

# 쿼리를 실행하고 실행 계획을 설명합니다.
explain_result = collection.find({"name": "Alice"}).explain()
print("Execution Plan and Stats:")
print(explain_result)
