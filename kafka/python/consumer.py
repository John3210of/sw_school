# from kafka import KafkaConsumer
# import json
# class MessageConsumer:
#     def __init__(self, broker, topic):
#         self.broker = broker
#         self.consumer = KafkaConsumer(
#             topic, # Topic to consume
#             bootstrap_servers=self.broker,
#             value_deserializer=lambda x: x.decode(
#             "utf-8"
#             ), # Decode message value as utf-8
#             group_id="my-group", # Consumer group ID
#             auto_offset_reset="earliest", # Start consuming from earliest available message
#             # enable_auto_commit=True, # Commit offsets automatically
#             enable_auto_commit=False, # Commit offsets automatically
#             )
#     def receive_message(self):
#         try:
#             for message in self.consumer:
#                 print(message.value)
#                 result = json.loads(message.value)
#                 for k, v in result.items():
#                     print(k, ":", v)
#                     # print(result["name"])
#                     # print(result["age"])
#         except Exception as e:
#             print(e)
#             # raise exc

# # 브로커와 토픽명을 지정한다.
# broker = ["localhost:9092"]
# topic = "exam-topic"
# cs = MessageConsumer(broker, topic)
# cs.receive_message()

from kafka import KafkaConsumer
import json

class MessageConsumer:
    def __init__(self, broker, topic):
        self.broker = broker
        self.consumer = KafkaConsumer(
            topic,  # Topic to consume
            bootstrap_servers=self.broker,
            value_deserializer=lambda x: x.decode("utf-8"),  # Decode message value as utf-8
            group_id="my-group",  # Consumer group ID
            auto_offset_reset="earliest",  # Start consuming from earliest available message
            enable_auto_commit=False,  # Disable auto commit
        )

    def receive_message(self):
        try:
            for message in self.consumer:
                try:
                    # 메시지 출력 (디버깅용)
                    print(f"Raw message received: {message.value}")
                    
                    # 메시지가 비어 있는지 확인하고 건너뛰기
                    if not message.value.strip():
                        print("Empty message received, skipping...")
                        continue

                    # JSON으로 디코딩
                    result = json.loads(message.value)
                    for k, v in result.items():
                        print(f"{k}: {v}")

                    # 메시지가 정상적으로 처리된 경우에만 오프셋 커밋
                    self.consumer.commit()

                except json.JSONDecodeError:
                    # JSON 디코딩 오류 발생 시 처리
                    print(f"Invalid JSON format for message: {message.value}")
                    continue  # 다음 메시지로 넘어감

                except Exception as e:
                    # 그 외 모든 예외 처리
                    print(f"Error processing message: {e}")
                    continue  # 오류 발생 시 다음 메시지로 넘어감

        except Exception as e:
            print(f"Fatal error: {e}")
            raise  # 치명적인 오류 발생 시 프로그램 중단 가능

# 브로커와 토픽명을 지정한다.
broker = ["localhost:9092"]
topic = "exam-topic"
cs = MessageConsumer(broker, topic)
cs.receive_message()
