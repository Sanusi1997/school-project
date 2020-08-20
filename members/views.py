from rest_framework import generics
from members.serializers import TeacherSerializer
from members.models import Teacher


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
