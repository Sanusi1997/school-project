from rest_framework import serializers
from members.models import Student, Teacher

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields=['first_name', 'last_name', 'subject_taught']





