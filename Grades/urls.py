from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Grades.views.grades_view import GradesList
from Grades.views.grades_view import GradesDetail

urlpatterns = [
    path('grades/', GradesList.as_view()),
    path('grades/<int:pk>', GradesDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)