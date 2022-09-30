from django.db import models

class Grades(models.Model):

    id = models.AutoField(primary_key=True)
    id_group = models.CharField(max_length = 30)
    id_student = models.CharField(max_length = 30)
    grade = models.DecimalField(max_digits=3, decimal_places=2)

    class Meta:
        app_label = 'Grades'