from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from apis.filters import TeacherFilter
from apis.models import Teacher
from apis.serializers import TeacherDetailSerializer, TeacherListSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all().prefetch_related('class_rooms')
    filter_backends = [DjangoFilterBackend]
    filterset_class = TeacherFilter

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TeacherDetailSerializer
        return TeacherListSerializer