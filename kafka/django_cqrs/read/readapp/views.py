from pymongo import MongoClient
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

client = MongoClient('mongodb://localhost:27017/')
db = client.cqrs
collection = db.books
class BookListView(APIView):
    def get(self, request, *args, **kwargs):
        # MongoDB에서 모든 책 데이터를 가져옴
        books = list(collection.find({}, {'_id': 0}))  # _id 필드를 제외하고 모든 데이터를 가져옴
        return Response(books, status=status.HTTP_200_OK)