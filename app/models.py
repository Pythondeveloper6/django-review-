from django.db import models

# Create your models here.

class MyData(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField(max_length=2000)
    done = models.BooleanField(default=False)
    created_date = models.DateTimeField()
    
    def __str__(self):
        return self.title

    