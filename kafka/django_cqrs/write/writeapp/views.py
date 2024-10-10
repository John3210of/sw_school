from rest_framework.response import Response
from rest_framework import viewsets, status
from .serializers import BookSerializer
from .models import *
import json
from kafka import KafkaProducer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def get_view_name(self):
        return "Write app Book List"

    def create(self, request, *args, **kwargs):
        data = request.data
        producer = KafkaProducer(
            bootstrap_servers='localhost:9092',
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        if isinstance(data, list):
            response_data = []
            for item in data:
                item['pages'] = int(item['pages'])
                item['price'] = int(item['price'])
                serializer = self.get_serializer(data=item)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                response_data.append(serializer.data)
                producer.send('books-topic', item)
            producer.flush()  # 메시지가 성공적으로 전송되었는지 확인
            producer.close()
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            data['pages'] = int(data['pages'])
            data['price'] = int(data['price'])
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            producer.send('books-topic', data)
            producer.flush()
            producer.close()
            return Response(serializer.data, status=status.HTTP_201_CREATED)