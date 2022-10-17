#! -*- coding: utf-8 -*-
import pika
import json
from Grades.models import Grades
from django_rabbitmq.mq import RabbitMQ

class CustomRabbit(RabbitMQ):

    def callback(self, ch, method, properties, body):
        print("[django-rabbitmq] Recibido %r" % body)
        data = json.loads(body)
        print("json", data)
        grade = Grades.objects.create(id_group=data['id_group'], id_student=data['id_student'], grade=data['grade'])
        grade.save()
        print("grade created")