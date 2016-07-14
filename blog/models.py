from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=120)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField()
    image = models.ImageField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title