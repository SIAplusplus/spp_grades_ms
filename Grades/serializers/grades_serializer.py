from rest_framework import serializers
from Grades.models.grades_model import Grades

class GradesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Grades
        fields = ['id', 'id_group', 'id_student', 'grade']
    
    def create(self, validated_data):

        grade = Grades(id_group = validated_data.get("id_group"),
                          id_student = validated_data.get("id_student"),
                          grade = validated_data.get("grade"))
        grade.save()
        return grade

    def update(self, instance, validated_data):

        instance.id_group = validated_data.get("id_group")
        instance.id_student = validated_data.get("id_student")
        instance.grade = validated_data.get("grade")
        instance.save()
        return instance

