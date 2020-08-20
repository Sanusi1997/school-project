from rest_framework import serializers
from members.models import Student, Teacher
from django.contrib.auth.models import User


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'subject_taught']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'department', 'has_graduated', 'student_email',
                  'date_of_entry', 'graduation_date']

    class Meta:
        model = User
        fields = ['id', 'username', 'subject_taught']