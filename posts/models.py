from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=8192)
    image = models.ImageField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
