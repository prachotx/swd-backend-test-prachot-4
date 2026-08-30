from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from apis.filters import StudentFilter
from apis.models import Student
from apis.serializers import StudentDetailSerializer, StudentListSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().select_related('class_room')
    filter_backends = [DjangoFilterBackend]
    filterset_class = StudentFilter

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return StudentDetailSerializer
        return StudentListSerializer