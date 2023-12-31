from django.db import models

class Developed(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField("date created")
    def __str__(self):
        return self.title

