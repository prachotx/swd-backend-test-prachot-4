from django.db import models

# ENUM


class Gender(models.TextChoices):
    MALE = "M", "Male"
    FEMALE = "F", "Female"
    OTHER = "O", "Other"


# TABLE


class School(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=10)
    address = models.TextField()

    class Meta:
        db_table = "schools"


class ClassRoom(models.Model):
    year_level = models.IntegerField()
    room = models.CharField(max_length=10)

    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name="classrooms"
    )

    class Meta:
        db_table = "classrooms"


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    gender = models.CharField(
        max_length=1, choices=Gender.choices, default=Gender.OTHER
    )

    classrooms = models.ManyToManyField(ClassRoom, related_name="teachers")

    class Meta:
        db_table = "teachers"


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    gender = models.CharField(
        max_length=1, choices=Gender.choices, default=Gender.OTHER
    )

    classroom = models.ForeignKey(
        ClassRoom, on_delete=models.CASCADE, related_name="students"
    )

    class Meta:
        db_table = "students"
