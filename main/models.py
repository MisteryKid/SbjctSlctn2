from django.db import models


class Account(models.Model):
    clsNb = models.IntegerField()
    Name = models.CharField(max_length=10)
    pw = models.IntegerField()

    def __str__(self):
        return self.Name