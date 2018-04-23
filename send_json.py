import sys,pika
import json
from base64 import b64encode, b64decode

credentials = pika.PlainCredentials(sys.argv[2], sys.argv[3])
connection = pika.BlockingConnection(pika.ConnectionParameters(host=sys.argv[1],
															   credentials = credentials))
channel = connection.channel()

channel.queue_declare(queue='hello_json')

image = open('../images.jpg','rb')
image_read = image.read()
image_64_encode = b64encode(image_read)
new_image = image_64_encode.decode('utf-8')

data = {
	"image": new_image
    }
data_string = json.dumps(data)

channel.basic_publish(exchange='',
	                    routing_key ='hello_json',
	                    body=data_string)
print(" [x] sent 'Hello world, Oscar T. gay!'")
print ('JSON:', data_string)

connection.close() 







