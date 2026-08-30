from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from apis.filters import ClassRoomFilter
from apis.models import ClassRoom
from apis.serializers import ClassRoomListSerializer
from apis.serializers import ClassRoomDetailSerializer


class ClassRoomViewSet(viewsets.ModelViewSet):
    queryset = ClassRoom.objects.all().prefetch_related("teachers", "students")
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClassRoomFilter

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ClassRoomDetailSerializer
        return ClassRoomListSerializer
