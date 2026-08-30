from django.db.models import Count
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from apis.models import School
from apis.serializers import SchoolDetailSerializer, SchoolListSerializer


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ["name"]

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.action == "retrieve":
            queryset = queryset.annotate(
                classroom_count=Count("class_rooms", distinct=True),
                student_count=Count("class_rooms__students", distinct=True),
                teacher_count=Count("class_rooms__teachers", distinct=True),
            )

        return queryset

    def get_serializer_class(self):
        if self.action == "retrieve":
            return SchoolDetailSerializer
        return SchoolListSerializer