from django.shortcuts import render
from Mixins_courses_app.models import Course
from Mixins_courses_app.serializers import CourseSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics,mixins

class CourseList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer = CourseSerializer
    def get(self, request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)

class Course_detail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer = CourseSerializer

    def get(self, request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)








