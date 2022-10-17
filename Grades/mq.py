import pika
import json
from Grades.models import Grades

class RabbitMQ(object):

    def __init__(self, host, port, virtual_host, user, password):
        credentials = pika.PlainCredentials(user, password)
        parameters = pika.ConnectionParameters(host=host, port=port, virtual_host=virtual_host, credentials=credentials)
        self.connection = pika.BlockingConnection(parameters)

    def start_mq(self, queue):
        channel = self.connection.channel()
        channel.queue_declare(queue=queue)

        channel.basic_consume(queue=queue, on_message_callback=self.callback, auto_ack=True)

        print('[django-rabbitmq] Esperando por mensajes. To exit press CTRL+C')
        channel.start_consuming()

    @staticmethod
    def callback(ch, method, properties, body):
        print("[django-rabbitmq] Recibido %r" % body)
        data = json.loads(body)
        print("json", data)
        grade = Grades.objects.create(id=data['id'], id_group=data['id_group'], id_student=data['id_student'], grade=data['grade'])
        grade.save()
        print("grade created")