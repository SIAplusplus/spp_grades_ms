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

    if properties.content_type == 'grade_created':
        grade = Grades.objects.create(id=data['id'], id_group=data['id_group'], id_student=data['id_student'], grade=data['grade'])
        grade.save()
        print("grade created")
    elif properties.content_type == 'grade_updated':
        grade = Grades.objects.get(id=data['id'])
        grade.title = data['title']

        grade.save()
        print("grade updated")
    elif properties.content_type == 'grade_deleted':
        grade = Grades.objects.get(id=data)

        print(grade)
        grade.delete()
        print("grade deleted")
channel.basic_consume(queue='spp_mq', on_message_callback=callback, auto_ack=True)
print("Started Consuming...")
channel.start_consuming()