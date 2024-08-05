from django.contrib import admin
from django.urls import path
from screening import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('submit_job_description/', views.submit_job_description, name='submit_job_description'),
    path('submit_resume/', views.submit_resume, name='submit_resume'),
    path('match_resume/', views.match_resume, name='match_resume'),
]
