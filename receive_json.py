import sys, pika
import json
from base64 import b64encode, b64decode

print(sys.argv[1])

connection = pika.BlockingConnection(pika.ConnectionParameters(host=sys.argv[1]))
channel = connection.channel()

channel.queue_declare(queue='hello_json')

def callback(ch, method, properties, body):
	data = json.loads(body)
	print(data)
	for image,value in data.items():
		image_64_decode = b64decode(value) 
		image_result = open('images_decode.jpg', 'wb') # create a writable image and write the decoding result
		image_result.write(image_64_decode)
	

channel.basic_consume(callback,
	                   queue='hello_json',
	                   no_ack=True)

print(' [*] waiting for messages. To exit press ctrl+c')
channel.start_consuming()