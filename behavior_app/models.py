# behavior_app/models.py
from django.db import models


class Behavior(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Note(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='notes')
    date = models.DateField(auto_now_add=True)  # Automatically adds the current date when a new note is created
    behavior = models.ForeignKey(Behavior, on_delete=models.CASCADE)
    notes = models.TextField()

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} - {self.date}"
