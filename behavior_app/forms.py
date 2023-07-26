from django import forms
from django.utils import timezone
from .models import Note, Student, Behavior


class DateInput(forms.DateInput):
    input_type = 'date'


class NoteForm(forms.ModelForm):
    behavior = forms.ModelChoiceField(queryset=Behavior.objects.all(), required=True)
    notes = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), required=True)

    class Meta:
        model = Note
        fields = ['behavior', 'notes']


class AddStudentsForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name']

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        if not first_name and not last_name:
            raise forms.ValidationError("Please provide either first name or last name.")
        return cleaned_data


class UploadCSVForm(forms.Form):
    csv_file = forms.FileField(label='Select a CSV file', help_text='File format: CSV')

    def clean_csv_file(self):
        csv_file = self.cleaned_data['csv_file']
        if not csv_file.name.endswith('.csv'):
            raise forms.ValidationError('File is not in CSV format')
        return csv_file
