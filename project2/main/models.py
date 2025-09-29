from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20, unique=True)  


    def __str__(self):
        return f"{self.name} ({self.student_id}) - {self.department}, {self.year}학년 {self.semester}학기"
