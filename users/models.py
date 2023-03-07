from django.contrib.auth.models import User
from django.db import models

class Assistant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_assistant = models.BooleanField(default=True)
    # otros campos

class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_professor = models.BooleanField(default=True)
    qr_code = models.CharField(max_length=255)
    # otros campos

class Attendance(models.Model):
    assistant = models.ForeignKey(Assistant, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)