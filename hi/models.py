# gold/models.py
from django.db import models

class ActivityLog(models.Model):
    action = models.CharField(max_length=255)
    amount = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action} - {self.amount} gold"
