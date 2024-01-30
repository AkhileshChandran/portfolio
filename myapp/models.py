
from django.db import models

class Review(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    review = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
