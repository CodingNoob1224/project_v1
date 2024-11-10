from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    birthday = models.DateField()
    department = models.CharField(max_length=100)
    registered_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
