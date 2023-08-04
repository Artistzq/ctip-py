import threading
from kafka import KafkaConsumer

from ..models.kafka_message import KafkaMessage
from ..models.StableDiffusionArgs import StableDiffusionArgs
from pydantic import parse_obj_as
import json


def text2img_kafka_consumer_task(topic, bootstrap_servers):
    consumer = KafkaConsumer(topic,
                             bootstrap_servers=bootstrap_servers,
                             auto_offset_reset='latest',
                             group_id = "group-" + topic,
                             enable_auto_commit=False)

    try:
        for message in consumer:
            # 在线程中处理消息，这里仅仅打印消息内容
            # print(f"Received message: {message.value.decode('utf-8')}")
            kafka_message = parse_obj_as(KafkaMessage, json.loads(message.value.decode('utf-8')))
            sd_args = parse_obj_as(StableDiffusionArgs, kafka_message.data)
            print(sd_args)
            # 手动提交偏移量，防止重复消费消息
            consumer.commit()

    except KeyboardInterrupt:
        print("Kafka consumer task cancelled.")
    except Exception as e:
        print(f"Kafka consumer error: {e}")

    finally:
        consumer.close()

def start_kafka_consumers(topic, bootstrap_servers, num_threads):
    kafka_threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=text2img_kafka_consumer_task, args=(topic, bootstrap_servers))
        thread.daemon = True  # 设置线程为守护线程，确保程序关闭时线程也会结束
        thread.start()
        kafka_threads.append(thread)

    return kafka_threads

def stop_kafka_consumers(kafka_threads):
    for thread in kafka_threads:
        thread.join()