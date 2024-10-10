from kafka.admin import KafkaAdminClient, NewTopic
from kafka.errors import TopicAlreadyExistsError

def create_topic_if_not_exists(topic_name):
    '''흠 지금은 굳이 클래스 형태까로까지는 필요 없긴 할듯 ?'''
    admin_client = KafkaAdminClient(bootstrap_servers='localhost:9092')
    topic_list = [NewTopic(name=topic_name, num_partitions=1, replication_factor=1)]
    try:
        admin_client.create_topics(new_topics=topic_list, validate_only=False)
        print(f"Topic '{topic_name}' created successfully.")
    except TopicAlreadyExistsError:
        print(f"Topic '{topic_name}' already exists.")
    finally:
        admin_client.close()