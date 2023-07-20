# behavior_app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Note, Behavior
from .forms import NoteForm


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    notes = Note.objects.filter(student=student)
    return render(request, 'student_detail.html', {'student': student, 'notes': notes})


def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('behavior_app:student-list')
    else:
        form = NoteForm()
    return render(request, 'note_form.html', {'form': form})


def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('behavior_app:student-list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'note_form.html', {'form': form})


def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('behavior_app:student-list')
    return render(request, 'note_confirm_delete.html', {'note': note})


def top_behaviors(request):
    behaviors = Behavior.objects.annotate(num_occurrences=Count('note')).order_by('-num_occurrences')[:5]
    return render(request, 'top_behaviors.html', {'behaviors': behaviors})
