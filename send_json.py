import sys,pika
import json

credentials = pika.PlainCredentials(sys.argv[2], sys.argv[3])
connection = pika.BlockingConnection(pika.ConnectionParameters(host=sys.argv[1],
															   credentials = credentials))
channel = connection.channel()

channel.queue_declare(queue='hello_json')
data = {
	"id":1,
	"name": "Oscar el homo mas homo",
	"description": "Es el gran homo"
    }
data_string = json.dumps(data)

channel.basic_publish(exchange='',
	                    routing_key ='hello_json',
	                    body=data_string)
print(" [x] sent 'Hello world, Oscar T. gay!'")
print ('JSON:', data_string)

connection.close() 







