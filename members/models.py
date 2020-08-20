from django.db import models

# Create your models here.


DEPARTMENT_TYPE = (
    ('SCIENCE', 'SCIENCE'),
    ('ARTS', 'ARTS'),
    ('COMMERCIAL', 'COMMERCIAL')
)

class Student(models.Model):
    first_name = models.CharField(max_length=100, blank=False, unique=True)
    last_name = models.CharField(max_length=100, blank=False, unique=True)
    department = models.CharField(max_length=100, choices=DEPARTMENT_TYPE)
    date_of_entry = models.DateField(null=True, blank= True)
    graduation_date = models.DateField(null=True, blank= True)
    student_email= models.CharField(max_length=100, blank=True, default=' ')
    has_graduated = models.BooleanField(default=False)

    def __str__(self):
        return '{}, {}'.format(self.first_name, self.last_name)

class Teacher(models.Model):
    first_name = models.CharField(max_length=100, blank=False, unique=True)
    last_name = models.CharField(max_length=100, blank=False, unique=True)
    subject_taught = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return '{}, {}'.format(self.first_name, self.last_name)


