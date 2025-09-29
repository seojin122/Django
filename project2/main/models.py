from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    department = models.CharField(max_length=100, blank=True)
    student_id = models.CharField(max_length=20, unique=True)  


    def __str__(self):
        return f"{self.name} ({self.student_id}) - {self.department}"
