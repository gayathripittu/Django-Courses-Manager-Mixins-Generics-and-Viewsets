from rest_framework import serializers
from Mixins_courses_app.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields='__all__'
        


