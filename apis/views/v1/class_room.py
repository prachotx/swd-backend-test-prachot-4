from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from apis.filters import ClassRoomFilter
from apis.models import ClassRoom
from apis.serializers import ClassRoomSerializer


class ClassRoomViewSet(viewsets.ModelViewSet):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer

    filter_backends = [
        DjangoFilterBackend,
    ]

    filterset_class = ClassRoomFilter