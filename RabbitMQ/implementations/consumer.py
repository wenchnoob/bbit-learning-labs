#Uncomment line above & run cell to save solution
#TODO Define class that implements consumerInterface & allows for the consumption of messages from rabbitMQ

import pika
import os
from RabbitMQ.interfaces.consumerInterface import consumerInterface
from typing import Any
import time

conParams = pika.URLParameters('amqp://localhost:5672')
connection = pika.BlockingConnection(parameters=conParams)
channel = connection.channel()

e = channel.exchange_declare('Test Exchange')
q = channel.queue_declare(queue='Test_Q')



class consumer(consumerInterface):
    def __init__(self, routing_key: str, **kwargs) -> None:
        super().__init__(routing_key, **kwargs)
        channel.queue_bind('Test_Q', 'Test Exchange', routing_key)

    def startConsuming(self):
        channel.basic_consume('Test_Q', lambda msg, x, y, z: print(z))
        try:
            channel.start_consuming()
        except KeyboardInterrupt:
            channel.stop_consuming()
            connection.close()


    def stopConsuming(self):
        channel.stop_consuming()
        connection.close()

c = consumer('__test')
c.startConsuming()
