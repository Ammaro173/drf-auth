from django.db import models

# Create your models here.


class Party(models.Model):
    title = models.CharField(max_length=200)
    describtion = models.TextField()

    def __str__(self):
        return self.title
