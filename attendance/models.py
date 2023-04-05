from django.db import models
# from validators import validate_email as validate_o6u_email



class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True) 
    courses = models.ManyToManyField('Course' , related_name= 'students')
    lectures = models.ManyToManyField('Lecture', through= 'Attendance')
    

    def __str__(self):
        return f"{self.id}"
    
    
    
class Course(models.Model):
    course_description = models.TextField()
    course_name = models.CharField(max_length=255)
    course_credit_hour = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.id}"


    
class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    courses = models.ManyToManyField('Course', related_name='doctors')
    
    def __str__(self):
        return f"{self.first_name}"


class Lecture(models.Model):
    #title = models.CharField(max_length=100)
    date = models.DateTimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='lectures')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lecture')

    def __str__(self):
        return f"{self.date} - {self.course.course_name} ({self.doctor.first_name} {self.doctor.last_name})" 
    


class Admin(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id}"
#povit tabl
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
   # present = models.BooleanField(default=False)
   
   
        
    def __str__(self):
        return f"{self.lecture_date}"

