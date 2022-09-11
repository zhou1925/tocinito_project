from django.db import models
from django.utils import timezone

class Sale(models.Model):
    date = models.DateField(default=timezone.now)
    amount = models.DecimalField(default=0, decimal_places=2, max_digits=10)

    def __str__(self):
        return str(self.amount)