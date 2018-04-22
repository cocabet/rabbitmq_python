import sys,pika
import json, base64

credentials = pika.PlainCredentials(sys.argv[2], sys.argv[3])
connection = pika.BlockingConnection(pika.ConnectionParameters(host=sys.argv[1],
															   credentials = credentials))
channel = connection.channel()

channel.queue_declare(queue='hello_json')

image = open('../images.jpg','rb')
image_read = image.read()
image_64_encode = base64.encodestring(image_read)

#data = {
#	"id":1,
#	"image": image_64_encode,
#	"description": "Es el gran homo"
#    }
#data_string = json.dumps(data)

channel.basic_publish(exchange='',
	                    routing_key ='hello_json',
	                    body=image_64_encode)
print(" [x] sent 'Hello world, Oscar T. gay!'")
#print ('JSON:', data_string)

connection.close() 







