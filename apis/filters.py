from django_filters import FilterSet

from apis.models import ClassRoom

class ClassRoomFilter(FilterSet):
    class Meta:
        model = ClassRoom
        fields = [
            'school',
        ]
