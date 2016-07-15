from django.db import models
from django.conf import settings
from django.utils.text import slugify


class PostQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)


def image_upload_to_post(instance, filename):
    title = instance.title
    slug = slugify(title)
    basename, file_extension = filename.split(".")
    new_filename = "%s-%s.%s" %(slug, instance.id, file_extension)
    return "blog/%s/%s" %(slug, new_filename)

class Post(models.Model):
    active = models.BooleanField(default=True)
    title = models.CharField(max_length=120)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField()
    image = models.ImageField(upload_to=image_upload_to_post, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

