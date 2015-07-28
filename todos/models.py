from django.db import models
from django.core.urlresolvers import reverse
from django.views.generic import ListView
class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True) 
    due = models.DateTimeField(null=True, blank=True) 
    created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)
    done = models.BooleanField(default=False)
    color = models.CharField(max_length=50, default="yellow")
    fontcolor = models.CharField(max_length=50, default="black")
    folder = models.ForeignKey('Folder', related_name= "notes", null=True, blank=True)
    tag = models.ManyToManyField('Tag', related_name='notes', null=True, blank=True)
    
    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk":self.pk})

        

class Folder(models.Model):
    title = models.CharField(max_length=255)
    color = models.CharField(max_length=50, default="purple")
    fontcolor = models.CharField(max_length=50, default="white")
    
    def __str__(self):
        return self.title
        
class Tag(models.Model):
    title = models.CharField(max_length=255)
    color = models.CharField(max_length=50, default="red")
    fontcolor = models.CharField(max_length=50, default="black")
    
    def __str__(self):
        return self.title

