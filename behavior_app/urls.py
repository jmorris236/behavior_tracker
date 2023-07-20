from django.urls import path
from .views import (
    student_list,
    student_detail,
    add_students_manually,
    delete_student,
    add_students_with_csv,
    notes_list,
    NoteAddView,  # Include the new view
)

app_name = 'behavior_app'

urlpatterns = [
    path('', student_list, name='default-page'),
    path('students/', student_list, name='student-list'),
    path('students/<int:pk>/', student_detail, name='student-detail'),
    path('students/add-manually/', add_students_manually, name='add-students-manually'),
    path('students/<int:pk>/delete/', delete_student, name='delete-student'),
    path('students/add-with-csv/', add_students_with_csv, name='add-students-with-csv'),
    path('students/<int:pk>/notes/', notes_list, name='notes-list'),

    # Use NoteAddView for "note-add"
    path('notes/add/<int:pk>/', NoteAddView.as_view(), name='note-add'),
]
