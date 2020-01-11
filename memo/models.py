from django.db import models


class Memo(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=300)
