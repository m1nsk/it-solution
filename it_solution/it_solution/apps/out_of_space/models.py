from django.db import models


class Message(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=1024)
    read_status = models.BooleanField(default=False)
