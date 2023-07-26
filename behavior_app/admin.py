from django.contrib import admin
from .models import Student, Note, Behavior

# Register your models here.
admin.site.register(Behavior)
admin.site.register(Student)
admin.site.register(Note)