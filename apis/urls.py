from django.urls import path
from apis.views.v1.school import SchoolViewSet
from apis.views.v1.class_room import ClassRoomViewSet

urlpatterns = [
    path(
        "v1/schools/",
        SchoolViewSet.as_view(),
        name="school-list",
    ),
    path(
        "v1/class-rooms/",
        ClassRoomViewSet.as_view(),
        name="class-room-list",
    ),
]