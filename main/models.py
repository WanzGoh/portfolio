from django.db import models

# Create your models here.
class Resume(models.Model):
    title = models.CharField(max_length = 100)
    date = models.CharField(max_length = 100)
    position = models.CharField(max_length = 150)
    content = models.TextField()
    def __str__(self):
	    return self.title


class Skill(models.Model):
    title = models.CharField(max_length = 150)
    value = models.IntegerField()
    def __str__(self):
	    return self.title

class Project(models.Model):
    title = models.CharField(max_length = 150)
    subject = models.CharField(max_length = 150)
    img_path = models.CharField(max_length = 255)
    def __str__(self):
	    return self.title




