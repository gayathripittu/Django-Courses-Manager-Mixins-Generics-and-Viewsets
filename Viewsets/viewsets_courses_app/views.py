from viewsets_courses_app.models import Course
from viewsets_courses_app.serializers import CourseSerializer
from rest_framework import viewsets


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


