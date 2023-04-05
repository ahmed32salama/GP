from django.urls import include, path
from rest_framework import routers
from .viewsets import*

router = routers.DefaultRouter()
router.register(r'student', StudentViewSet)
router.register(r'doctor', DoctorViewSet)
#router.register(r'attendance', AttendanceViewSet)
router.register(r'lecture', LectureViewSet)
router.register(r'course', CourseViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('attendance/<int:id>/', Attendance.as_view(), name='attendance-by-student'),
]
