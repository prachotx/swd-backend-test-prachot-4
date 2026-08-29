from django_filters import CharFilter, FilterSet, NumberFilter

from apis.models import ClassRoom, Teacher


class ClassRoomFilter(FilterSet):
    class Meta:
        model = ClassRoom
        fields = [
            'school',
        ]


class TeacherFilter(FilterSet):
    school = NumberFilter(field_name='class_rooms__school', lookup_expr='exact')
    classroom = NumberFilter(field_name='class_rooms', lookup_expr='exact')
    first_name = CharFilter(field_name='first_name', lookup_expr='icontains')
    last_name = CharFilter(field_name='last_name', lookup_expr='icontains')
    gender = CharFilter(field_name='gender', lookup_expr='exact')

    class Meta:
        model = Teacher
        fields = []
