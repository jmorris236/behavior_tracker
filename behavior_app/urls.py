
# behavior_app/urls.py
from django.urls import path
from .views import (
    student_list,
    student_detail,
    note_create,
    note_update,
    note_delete,
    top_behaviors,
)

app_name = 'behavior_app'

urlpatterns = [
    path('students/', student_list, name='student-list'),
    path('students/<int:pk>/', student_detail, name='student-detail'),
    path('notes/add/', note_create, name='note-add'),
    path('notes/<int:pk>/edit/', note_update, name='note-edit'),
    path('notes/<int:pk>/delete/', note_delete, name='note-delete'),
    path('top-behaviors/', top_behaviors, name='top-behaviors'),

    # Empty path acts as the catch-all or default URL
    path('', student_list, name='default-page'),
]
