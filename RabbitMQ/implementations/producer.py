#Uncomment line above & run cell to save solution
#TODO Define class that implements producerInterface & allows for the publishing of messages to rabbitMQ
import pika
import os
from RabbitMQ.interfaces.producerInterface import producerInterface
from typing import Any
import time

conParams = pika.URLParameters('amqp://localhost:5672')
connection = pika.BlockingConnection(parameters=conParams)
channel = connection.channel()
channel.exchange_declare('Test Exchange')

#We can then publish data to that exchange using the basic_publish method
# channel.basic_publish('Test Exchange', 'Test_route', 'Hi')

class producer(producerInterface):
    def __init__(self, routing_key : str, pub_delay : int, message_producer : Any) -> None:
        self.count = 0
        self.routing_key = routing_key
        self.pub_delay = pub_delay

    def startPublishing(self):
        while True:
            channel.basic_publish('Test Exchange', self.routing_key, f'message {self.count}')
            self.count+=1
            time.sleep(self.pub_delay)

p = producer('__test', 2, None)
p.startPublishing()
