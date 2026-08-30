from rest_framework import serializers

from .models import ClassRoom, School, Student, Teacher


class SchoolListSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ["id", "name", "short_name", "address"]


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
        fields = ["id", "school", "year_level", "room"]


class ClassRoomMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ["id", "year_level", "room"]


class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "first_name", "last_name", "gender", "classroom"]


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
    classroom = ClassRoomMiniSerializer(read_only=True)

    class Meta:
        model = Student
        fields = ["id", "first_name", "last_name", "gender", "classroom"]


class TeacherDetailSerializer(serializers.ModelSerializer):
    classrooms = ClassRoomMiniSerializer(many=True, read_only=True)

    class Meta:
        model = Teacher
        fields = ["id", "first_name", "last_name", "gender", "classrooms"]
