from django.db import models


class Answer(models.Model):
    x = models.CharField(max_length=1000)
    f = models.CharField(max_length=1000)
