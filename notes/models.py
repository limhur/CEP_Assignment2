from django.db import models
from django.views.generic import ListView 
from django.core.urlresolvers import reverse

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True) #not a required field
    due = models.DateTimeField(null=True, blank=True) #due datetime is optional
    created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)
    done = models.BooleanField(default=False)
    color = models.CharField(max_length=50, default="yellow")
    fontcolor = models.CharField(max_length=50, default="black")
    #folder is optional
    folder = models.ForeignKey('Folder', related_name= "notes", null=True, blank=True)
    #tag is optional
    tag = models.ManyToManyField('Tag', related_name='notes', null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk":self.pk})

class NoteList(ListView):
    #https://docs.djangoproject.com/en/1.7/topics/class-based-views/generic-display/
    model = Note
    
    def get_queryset(self):
        folder = self.kwargs['folder']
        if folder == '':
            return Note.objects.all()
        else:
            return Note.objects.filter(folder__title__iexact=folder)


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