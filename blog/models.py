from django.db import models

class Blog(models.Model):
    title=models.CharField(max_length=100)
    pub_date=models.DateTimeField(auto_now=True)
    blogpic = models.ImageField(upload_to="images/")
    body=models.TextField()
