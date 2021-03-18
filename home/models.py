from django.db import models


# Create your models here.

class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=600)
    content = models.TextField()
    short_desc=models.CharField(max_length=200, default="")
    slug = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=50)
    review = models.TextField()
    image = models.FileField(upload_to='static/reviewimg',default = 'static/reviewimg/no-img.jpg')

    def __str__(self):
        return self.name+" "+self.review