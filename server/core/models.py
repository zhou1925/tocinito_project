from django.db import models

class Weather(models.Model):
    data = models.TextField()

    def __str__(self):
        return self.data
