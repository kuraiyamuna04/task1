from django.db import models


class User(models.Model):
    email = models.EmailField(max_length=200)
    username = models.CharField(max_length=300)
    password = models.CharField(max_length=300)

    def __str__(self):
        return self.email

