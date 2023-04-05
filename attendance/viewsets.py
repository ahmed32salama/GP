from django.shortcuts import render
from rest_framework import viewsets
from .models import Attendance
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    
class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
class LectureViewSet(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    

class Attendance(APIView):
    
    # return lec id from doctor
    def get(self,request,*args,**kwargs):
        # print args and kwargs to see what parameters url passed.
        print(args)
        print(kwargs)
        id = kwargs.get('id')
        return Response(id)
    
    def post(self,request,*args,**kwargs):
        # print args and kwargs to see what parameters url passed.
        print(args)
        print(kwargs)
        id = kwargs.get('id')
        return Response(id)

        


    
