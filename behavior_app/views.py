# behavior_app/views.py
import csv
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Note, Behavior
from .forms import NoteForm, BehaviorForm

# behavior_app/views.py
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import NoteForm
from .models import Student


class NoteAddView(FormView):
    template_name = 'note_form.html'
    form_class = NoteForm
    success_url = reverse_lazy('behavior_app:student-list')

    def form_valid(self, form):
        student_id = self.kwargs['pk']
        student = get_object_or_404(Student, pk=student_id)
        form.instance.student = student
        form.save()
        return super().form_valid(form)


def default_page(request):
    return render(request, 'default_page.html')


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    notes = Note.objects.filter(student=student).order_by('-date')
    return render(request, 'student_detail.html', {'student': student, 'notes': notes})


def add_students_manually(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        student = Student.objects.create(first_name=first_name, last_name=last_name)
        return redirect('behavior_app:student-list')
    return render(request, 'add_students_manually.html')


def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('behavior_app:student-list')
    return render(request, 'delete_student.html', {'student': student})


def add_students_with_csv(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']
        decoded_file = csv_file.read().decode('utf-8')
        csv_reader = csv.reader(decoded_file.splitlines(), delimiter=',')
        next(csv_reader)  # Skip header row
        for row in csv_reader:
            first_name, last_name = row
            Student.objects.create(first_name=first_name, last_name=last_name)
        return redirect('behavior_app:student-list')
    return render(request, 'add_students_with_csv.html')


def notes_list(request, pk):
    student = get_object_or_404(Student, pk=pk)
    notes = Note.objects.filter(student=student).order_by('-date')
    return render(request, 'notes_list.html', {'student': student, 'notes': notes})
