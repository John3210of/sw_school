from pymongo import MongoClient
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

def get_mongo_connection():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.cqrs
    return client, db

class BookViewSet(viewsets.ViewSet):
    def get_view_name(self):
        return "Read app Book List server4"
    def list(self, request):
        client, db = get_mongo_connection()
        collection = db.books
        books = list(collection.find({}, {'_id': 0}))
        client.close()
        return Response(books, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        client, db = get_mongo_connection()
        collection = db.books
        
        book = collection.find_one({'id': int(pk)}, {'_id': 0})
        client.close()
        if book:
            return Response(book, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)