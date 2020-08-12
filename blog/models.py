from django.db import models

class Blog(models.Model):
    title=models.CharField(max_length=100)
    pub_date=models.DateTimeField(auto_now=True)
    blogpic = models.ImageField(upload_to="images/")
    body=models.TextField()

    def summary(self):
        return self.body[:100]


    def __str__(self):
        return self.title

    def pubdate(self):
        return self.pub_date.strftime('%b %e %Y')
