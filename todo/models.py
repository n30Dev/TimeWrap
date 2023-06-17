from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    title = models.CharField(verbose_name='Title', max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(verbose_name='Done', default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
