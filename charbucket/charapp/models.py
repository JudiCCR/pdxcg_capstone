from django.db import models
from tinymce import models as tinymce_models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, related_name = 'posts', on_delete = models.CASCADE)
    text = tinymce_models.HTMLField()
    title = models.CharField(max_length = 50, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add = True)
    upload = models.FileField(upload_to='uploads/', blank = True, null = True)
    

    def __str__(self):
        return f'{self.user.username} - {self.text}'

class Comment(models.Model):
    user = models.ForeignKey(User, related_name = 'comments', on_delete = models.CASCADE)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add = True)
    post = models.ForeignKey(Post, related_name = 'comments', on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.user.username}: {self.text}'