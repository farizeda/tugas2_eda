from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

class TodoListAttributes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_finished = models.BooleanField(default=False)
 
