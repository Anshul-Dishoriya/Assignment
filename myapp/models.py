from django.db import models


class Reminder(models.Model):
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()

    def __str__(self):
        return f"{self.date} - {self.time}: {self.message}"