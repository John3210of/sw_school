from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from .serializers import BookSerializer
from .models import *

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    qs = len(queryset)
    print("*********************")
    print(qs)
    print("*********************")
    serializer_class = BookSerializer

    # 데이터가 리스트로 들어오는 경우 처리하기 위해 create 메소드를 오버라이딩
    def create(self, request, *args, **kwargs):
        data = request.data

        if isinstance(data, list):
            response_data = []
            for item in data:
                item['pages'] = int(item['pages'])
                item['price'] = int(item['price'])
                serializer = self.get_serializer(data=item)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                response_data.append(serializer.data)
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            data['pages'] = int(data['pages'])
            data['price'] = int(data['price'])
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
