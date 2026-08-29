from apis.models import School
from apis.serializers import SchoolListSerializer
from apis.serializers import SchoolDetailSerializer
from rest_framework.filters import SearchFilter
from rest_framework import viewsets
from django.db.models import Count

class SchoolViewSet(viewsets.ModelViewSet):
    serializer_class = SchoolListSerializer

    filter_backends = [
        SearchFilter
    ]

    search_fields = [
        "name"
    ]

    def get_queryset(self):
        queryset = School.objects.all()

        if self.action == "retrieve":
            queryset = queryset.annotate(
                classroom_count=Count(
                    "class_rooms",
                    distinct=True
                ),
                student_count=Count(
                    "class_rooms__students",
                    distinct=True
                ),
                teacher_count=Count(
                    "class_rooms__teachers",
                    distinct=True
                ),
            )

        return queryset

    def get_serializer_class(self):
        if self.action == "retrieve":
            return SchoolDetailSerializer

        return SchoolListSerializer