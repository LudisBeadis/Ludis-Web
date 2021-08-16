from django.db import models

class Message(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField(max_length=2000)
    def __str__(self):
        return self.name