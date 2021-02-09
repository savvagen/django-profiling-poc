from django.db import models
from author.models import Author


class Article(models.Model):
    title = models.CharField(max_length=120)
    subject = models.CharField(max_length=120)
    body = models.TextField(max_length=3024, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, auto_created=True)
    author = models.ForeignKey(Author, related_name='author', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
