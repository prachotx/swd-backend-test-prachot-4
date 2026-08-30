from rest_framework import serializers

from .models import ClassRoom, School, Student, Teacher


class SchoolListSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"


class SchoolDetailSerializer(serializers.ModelSerializer):
    classroom_count = serializers.IntegerField(read_only=True)
    student_count = serializers.IntegerField(read_only=True)
    teacher_count = serializers.IntegerField(read_only=True)

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


class ClassRoomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = "__all__"


class ClassRoomMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ["id", "year_level", "room"]


class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "first_name", "last_name", "gender", "class_room"]


class TeacherListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ["id", "first_name", "last_name", "gender"]


class ClassRoomDetailSerializer(serializers.ModelSerializer):
    teachers = TeacherListSerializer(many=True, read_only=True)
    students = StudentListSerializer(many=True, read_only=True)

    class Meta:
        model = ClassRoom
        fields = [
            "id",
            "school",
            "year_level",
            "room",
            "teachers",
            "students",
        ]


class StudentDetailSerializer(serializers.ModelSerializer):
    class_room = ClassRoomMiniSerializer(read_only=True)

    class Meta:
        model = Student
        fields = ["id", "first_name", "last_name", "gender", "class_room"]


class TeacherDetailSerializer(serializers.ModelSerializer):
    class_rooms = ClassRoomMiniSerializer(many=True, read_only=True)

    class Meta:
        model = Teacher
        fields = ["id", "first_name", "last_name", "gender", "class_rooms"]
