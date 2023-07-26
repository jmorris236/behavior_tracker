# behavior_app/urls.py
from django.urls import path
from . import views
from django.views.generic import View



app_name = 'behavior_app'

urlpatterns = [
    path('', views.default_page, name='default-page'),
    path('student', views.student_list, name='student-list'),
    path('student/<int:pk>/', views.student_detail, name='student-detail'),
    path('student/add/', views.student_add, name='student-add'),
    path('student/<int:pk>/delete/', views.student_delete, name='delete-student'),
    path('student/<int:pk>/add_note/', views.note_add, name='note-add'),
    path('note/<int:pk>/delete/', views.note_delete, name='note-delete'),

    path('student/<int:pk>/notes_list/', views.NotesListView.as_view(), name='notes-list'),

]

