from django.db import models

class Jobs(models.Model):
    image = models.ImageField(upload_to="images/")
    header =models.CharField(max_length=100)
    summary = models.CharField(max_length=200)
