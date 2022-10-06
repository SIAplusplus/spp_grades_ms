import json
import pika

from Grades.models import Grades

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', heartbeat=600, blocked_connection_timeout=300))
channel = connection.channel()
channel.queue_declare(queue='spp_mq')

def callback(ch, method, properties, body):
    print("Received in grades...")
    print(body)
    data = json.loads(body)
    print(data)

    if properties.content_type == 'quote_created':
        quote = Quote.objects.create(id=data['id'], title=data['title'])
        quote.save()
        print("quote created")
    elif properties.content_type == 'quote_updated':
        quote = Quote.objects.get(id=data['id'])
        quote.title = data['title']

        quote.save()
        print("quote updated")
    elif properties.content_type == 'quote_deleted':
        quote = Quote.objects.get(id=data)

        print(quote)
        quote.delete()
        print("quote deleted")
channel.basic_consume(queue='spp_mq', on_message_callback=callback, auto_ack=True)
print("Started Consuming...")
channel.start_consuming()