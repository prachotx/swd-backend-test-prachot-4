from rest_framework import serializers
from .models import School
from .models import ClassRoom
from .models import Student
from .models import Teacher

class SchoolListSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"

class SchoolDetailSerializer(serializers.ModelSerializer):

    classroom_count = serializers.IntegerField(
        read_only=True
    )

    student_count = serializers.IntegerField(
        read_only=True
    )

    teacher_count = serializers.IntegerField(
        read_only=True
    )

    class Meta:
        model = School
        fields = [
            "id",
            "name",
            "short_name",
            "address",
            "classroom_count",
            "student_count",
            "teacher_count",
        ]
        
class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = "__all__"

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"
