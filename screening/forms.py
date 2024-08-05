from django import forms
from .models import JobDescription, Resume

class JobDescriptionForm(forms.ModelForm):
    class Meta:
        model = JobDescription
        fields = ['title', 'description']

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['candidate_name', 'resume_text']
