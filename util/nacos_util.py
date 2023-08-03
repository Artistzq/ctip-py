from nacos import NacosClient
import threading
import time


class NacosRegister:
    
    def __init__(self, nacos_addr):
        self.client = NacosClient(nacos_addr)
        self.pool = set()
    
    def register_new_service(self, service_name, ip, port):
        if service_name + ip + str(port) in self.pool:
            print("服务 {} 已注册到 {}:{}，无需重复".format(service_name, ip, port))
            return
        
        self.client.add_naming_instance(service_name, ip, port)
        self.pool.add(service_name + ip + str(port))
        thread = threading.Thread(target=self.heartbeat, kwargs={"service_name": service_name, "ip": ip, "port": port}, name=service_name + "")
        thread.start()
    
    def heartbeat(self, service_name, ip, port):
        while True:
            # 向Nacos发送心跳
            self.client.send_heartbeat(service_name, ip, port)
            time.sleep(5)  # 每隔5秒发送一次心跳
            print("heat beat.")
            
nacosRegister = NacosRegister("localhost:8848")