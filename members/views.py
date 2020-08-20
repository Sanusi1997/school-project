from rest_framework import generics
from members.serializers import TeacherSerializer, StudentSerializer
from members.models import Teacher, Student


class Teacher_List(generics.ListCreateAPIView):

    """
    List all teachers, or create a new teacher
    """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class Teacher_Detail(generics.RetrieveUpdateDestroyAPIView):
   
    """
    Retrieve, update or delete a teacher.
    """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class Student_List(generics.ListCreateAPIView):
   
    """
    List all students, or create a new student
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class Student_Detail(generics.RetrieveUpdateDestroyAPIView):

    """
    Retrieve, update or delete a student.
    """
   
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


