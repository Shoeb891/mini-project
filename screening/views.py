from django.shortcuts import render, redirect
from .forms import JobDescriptionForm, ResumeForm
from .models import JobDescription, Resume
from .utils import calculate_similarity
from django.contrib import messages

def submit_job_description(request):
    if request.method == 'POST':
        form = JobDescriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job Description submitted successfully.')
            return redirect('submit_resume')
    else:
        form = JobDescriptionForm()
    return render(request, 'submit_job_description.html', {'form': form})

def submit_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Resume submitted successfully.')
            return redirect('match_resume')
    else:
        form = ResumeForm()
    return render(request, 'submit_resume.html', {'form': form})

def match_resume(request):
    if request.method == 'POST':
        job = JobDescription.objects.last()  # Get the most recent job description
        resumes = Resume.objects.all()

        results = []
        for resume in resumes:
            similarity_score = calculate_similarity(job.description, resume.resume_text)
            results.append({
                'candidate_name': resume.candidate_name,
                'similarity_score': similarity_score,
            })

        return render(request, 'match_results.html', {'results': results})
    return render(request, 'match_resume.html')
