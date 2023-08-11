host = "127.0.0.1"
port = 7999
service_name='object-detect-service'
ip = host

class Kafka:
    bootstrap_servers = 'localhost:9092'
    topic = 'text_to_img_export'
    num_threads = 1  # 设置线程数量

kafka = Kafka()