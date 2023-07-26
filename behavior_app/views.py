# behavior_app/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Note
from .forms import NoteForm, AddStudentsForm, UploadCSVForm
from django.views.generic import View


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    notes = student.notes.all()

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.student = student
            note.save()
            return redirect('behavior_app:student-detail', pk=pk)
    else:
        form = NoteForm()



    context = {
        'student': student,
        'notes': notes,
        'form': form,
    }
    return render(request, 'student_detail.html', context)


def student_add(request):
    if request.method == 'POST':
        form = AddStudentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('behavior_app:student-list')
    else:
        form = AddStudentsForm()

    context = {
        'form': form,
    }
    return render(request, 'add_student.html', context)


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('behavior_app:student-list')

    context = {
        'student': student,
    }
    return render(request, 'delete_student.html', context)


def note_add(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.student = student
            note.save()
            return redirect('behavior_app:student-detail', pk=pk)
    else:
        form = NoteForm()

    context = {
        'student': student,
        'form': form,
    }
    return render(request, 'note_form.html', context)


def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    student_pk = note.student.pk
    if request.method == 'POST':
        note.delete()
        return redirect('behavior_app:student-detail', pk=student_pk)

    context = {
        'note': note,
    }
    return render(request, 'note_confirm_delete.html', context)

def default_page(request):
    return render(request, 'default_page.html')


class NotesListView(View):
    template_name = 'notes_list.html'

    def get(self, request, *args, **kwargs):
        student = Student.objects.get(pk=self.kwargs['pk'])
        notes = student.notes.all()

        context = {
            'student': student,
            'notes': notes,
        }
        return render(request, self.template_name, context)
