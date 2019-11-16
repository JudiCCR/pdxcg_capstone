from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, related_name = 'posts', on_delete = models.CASCADE)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add = True)

