from apis.models import School
from apis.serializers import SchoolSerializer
from rest_framework.filters import SearchFilter
from rest_framework import viewsets

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    filter_backends = [
        SearchFilter
    ]

    search_fields = [
        "name"
    ]