from rest_framework import serializers
from Generics_courses_app.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields='__all__'
        


