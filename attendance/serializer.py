from rest_framework import serializers
from .models import *




class StudentSerializer(serializers.ModelSerializer):
    courses = serializers.PrimaryKeyRelatedField(many=True, queryset=Course.objects.all())
    #lectures = serializers.PrimaryKeyRelatedField(many=True, queryset=Lecture.objects.all())
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'email', 'courses']


class CourseSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True)
   
    class Meta:
        model = Course
        fields = ['id', 'course_description', 'course_name', 'course_credit_hour', 'students' , 'doctors' ]
        
        
class DoctorSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)
    class Meta:
        model = Doctor
        fields = ['id', 'first_name', 'last_name', 'email' , 'courses' ]

class LectureSerializer(serializers.ModelSerializer):
    doctor = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all())
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    class Meta:
        model = Lecture
        fields = ['id', 'date', 'course', 'doctor' ]



class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['id', 'first_name', 'last_name', 'password']



        




