from django.db import models
from django.contrib.auth.models import User

class Runner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.location}"

class RunnerService(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class ErrandRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    runner = models.ForeignKey(Runner, on_delete=models.SET_NULL, null=True)
    service = models.ForeignKey(RunnerService, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(max_length=50, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Errand for {self.user.username} - {self.service.name}"