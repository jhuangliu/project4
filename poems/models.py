
# Create your models here.

# This inherits from models.model
from django.db import models

class Poem(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    body = models.TextField()
    owner = models.ForeignKey(
        'users.User', related_name='poems', on_delete=models.CASCADE, default='')

    def __repr__(self):
        return self.title

    # dunder string method
    def __str__(self):
        return self.title
