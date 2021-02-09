from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    date_created = models.DateTimeField(auto_created=True, auto_now_add=True)

    def __str__(self):
        return self.name
