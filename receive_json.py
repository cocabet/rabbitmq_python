import sys, pika
import json

print(sys.argv[1])

connection = pika.BlockingConnection(pika.ConnectionParameters(host=sys.argv[1]))
channel = connection.channel()

channel.queue_declare(queue='hello_json')

def callback(ch, method, properties, body):
	decoded = json.loads(body)
	print(decoded)

channel.basic_consume(callback,
	                   queue='hello_json',
	                   no_ack=True)

print(' [*] waiting for messages. To exit press ctrl+c')
channel.start_consuming()