from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apis.views.v1.classroom import ClassRoomViewSet
from apis.views.v1.school import SchoolViewSet
from apis.views.v1.student import StudentViewSet
from apis.views.v1.teacher import TeacherViewSet

router = DefaultRouter()
router.register(r'schools', SchoolViewSet, basename='school')
router.register(r'classrooms', ClassRoomViewSet, basename='classroom')
router.register(r'students', StudentViewSet, basename='student')
router.register(r'teachers', TeacherViewSet, basename='teacher')

urlpatterns = [
    path('v1/', include((router.urls, 'v1'), namespace='v1')),
]