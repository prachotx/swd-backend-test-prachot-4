from django_filters import CharFilter, FilterSet, NumberFilter

from apis.models import ClassRoom, Student, Teacher


class ClassRoomFilter(FilterSet):
    school = NumberFilter(field_name="school", lookup_expr="exact")

    class Meta:
        model = ClassRoom
        fields = []


class TeacherFilter(FilterSet):
    school = NumberFilter(field_name="classrooms__school", lookup_expr="exact")
    classroom = NumberFilter(field_name="classrooms", lookup_expr="exact")
    first_name = CharFilter(field_name="first_name", lookup_expr="icontains")
    last_name = CharFilter(field_name="last_name", lookup_expr="icontains")
    gender = CharFilter(field_name="gender", lookup_expr="exact")

    class Meta:
        model = Teacher
        fields = []


class StudentFilter(FilterSet):
    school = NumberFilter(field_name="classroom__school", lookup_expr="exact")
    classroom = NumberFilter(field_name="classroom", lookup_expr="exact")
    first_name = CharFilter(field_name="first_name", lookup_expr="icontains")
    last_name = CharFilter(field_name="last_name", lookup_expr="icontains")
    gender = CharFilter(field_name="gender", lookup_expr="exact")

    class Meta:
        model = Student
        fields = []
