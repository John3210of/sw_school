from rest_framework.response import Response
from rest_framework import viewsets, status
from .serializers import BookSerializer
from .models import *
from kafka import KafkaProducer
import json
from kafka.admin import KafkaAdminClient, NewTopic
from kafka.errors import TopicAlreadyExistsError

def create_topic_if_not_exists(topic_name):
    admin_client = KafkaAdminClient(bootstrap_servers='localhost:9092')
    topic_list = [NewTopic(name=topic_name, num_partitions=1, replication_factor=1)]
    try:
        admin_client.create_topics(new_topics=topic_list, validate_only=False)
        print(f"Topic '{topic_name}' created successfully.")
    except TopicAlreadyExistsError:
        print(f"Topic '{topic_name}' already exists.")
    finally:
        admin_client.close()

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        producer = KafkaProducer(
            bootstrap_servers='localhost:9092',
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        create_topic_if_not_exists('books-topic')
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
        

# kafka 미적용
# class BookViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

#     # 데이터가 리스트로 들어오는 경우 처리하기 위해 create 메소드를 오버라이딩
#     def create(self, request, *args, **kwargs):
#         data = request.data

#         if isinstance(data, list):
#             response_data = []
#             for item in data:
#                 item['pages'] = int(item['pages'])
#                 item['price'] = int(item['price'])
#                 serializer = self.get_serializer(data=item)
#                 serializer.is_valid(raise_exception=True)
#                 self.perform_create(serializer)
#                 response_data.append(serializer.data)
#             return Response(response_data, status=status.HTTP_201_CREATED)
#         else:
#             data['pages'] = int(data['pages'])
#             data['price'] = int(data['price'])
#             serializer = self.get_serializer(data=data)
#             serializer.is_valid(raise_exception=True)
#             self.perform_create(serializer)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)