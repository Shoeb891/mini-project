from django.db import models

class JobDescription(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class Resume(models.Model):
    candidate_name = models.CharField(max_length=255)
    resume_text = models.TextField()

    def __str__(self):
        return self.candidate_name
