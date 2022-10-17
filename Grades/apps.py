from django.apps import AppConfig
from django_rabbitmq.mq import RabbitMQ


class GradesConfig(AppConfig):
    name = 'Grades'
    
    def ready(self):
        from Grades.mq import CustomRabbit
        RabbitMQ.callback = CustomRabbit.callback
