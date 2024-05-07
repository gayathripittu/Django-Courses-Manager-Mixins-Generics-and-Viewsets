
from Generics_courses_app.models import Course
from Generics_courses_app.serializers import CourseSerializer
from rest_framework import generics

class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer = CourseSerializer

class Course_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer = CourseSerializer









