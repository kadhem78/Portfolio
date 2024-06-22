from django.db import models
from taggit.managers import TaggableManager

class Project(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(null=True , blank=True)
    description = models.TextField(default='')
    thumbnail = models.ImageField(upload_to='projects')
    video = models.URLField(max_length=200, null=True , blank=True)
    github = models.URLField(max_length=200)
    demo = models.URLField(max_length=200 , null=True , blank=True)
    objects = models.Manager()
    tags = TaggableManager()
    def __str__(self) : 
        return self.name



class Skill(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default='' , null=True , blank=True)

    def __str__(self) : 
        return self.name


class Account(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.name

class Message(models.Model):
    email = models.EmailField(max_length=254)
    subject = models.CharField( max_length=50)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_readed = models.BooleanField(default=False)



    def __str__(self):
        return self.email
    
