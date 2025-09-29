from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'department', 'student_id']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '이름을 입력하세요'}),
            'department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '학과을 입력하세요'}),
            'student_id': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '학번을 입력하세요'}),
        }
        labels = {
            'name': '이름',
            'department': '학과',
            'student_id': '학번',
        }

