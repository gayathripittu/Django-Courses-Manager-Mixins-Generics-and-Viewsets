from rest_framework import serializers
from viewsets_courses_app.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields='__all__'



        