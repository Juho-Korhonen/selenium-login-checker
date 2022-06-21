from django.db import models

# Create your models here.
class About_me(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


class Project(models.Model):
    title = models.CharField(max_length=100)
    explanation = models.TextField(max_length=200)
    github_link = models.CharField(max_length=100)