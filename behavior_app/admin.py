from django.contrib import admin
from .models import Student, Behavior, Note

# Register your models here.
admin.site.register(Student)
admin.site.register(Behavior)
admin.site.register(Note)
