# -*- coding: utf-8 -*-

import pika
from weather import weather
import utility

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='rpc_queue')
dicts = utility.create_dictionaries()
def on_request(ch, method, props, body):
    
    # nput = ["",""]
    # n = str(body)

    # nput = n.split(', ')
    # current_weather = weather("Toronto", "CA")
    
    # response = current_weather.toString()
    
    n = body.decode()
    nput = n.split(', ')
    if(weather('Toronto', 'CA').weather == "Clouds"):
        if(nput[0] == 'driver'):
            print("[.] Received requests from 'driver'")
            response = dicts[0][nput[1]]
            
            ch.basic_publish(exchange='',
                             routing_key=props.reply_to,
                             properties=pika.BasicProperties(correlation_id = \
                                                                 props.correlation_id),
                             body=str(response))
            ch.basic_ack(delivery_tag=method.delivery_tag)
    
        elif(nput[0] == 'client'):
            print("[.] Received requests from 'client'")
            response = dicts[1][nput[1]]
            
            ch.basic_publish(exchange='',
                             routing_key=props.reply_to,
                             properties=pika.BasicProperties(correlation_id = \
                                                                 props.correlation_id),
                             body=str(response))
            ch.basic_ack(delivery_tag=method.delivery_tag)
    else:
        response = "No vehicles are being dispatched since it is not snowing"

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='rpc_queue', on_message_callback=on_request)

print(" [x] Awaiting RPC requests")
channel.start_consuming()