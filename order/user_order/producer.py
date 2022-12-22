import pika
import json

params = pika.URLParameters('amqps://nshzwgly:jdm7g6mjKgWSX4_5Nm14VEOMxKp-Gbn4@dingo.rmq.cloudamqp.com/nshzwgly')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='boss', body=json.dumps(body), properties=properties)