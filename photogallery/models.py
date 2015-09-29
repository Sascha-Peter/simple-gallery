"""This file contains all models for the photo gallery

@author: Sascha Peter <sascha.o.peter@gmail.com>
@version: 0.1.0
@since: 2015-09-28
"""
from django.db import models
from taggit.managers import TaggableManager


class Photo(models.Model):
    """Photo model"""
    title = models.CharField(max_length=140)
    location = models.CharField(max_length=250)
    photo = models.ImageField(upload_to="photo")
    caption = models.TextField()
    date = models.DateField()
    upload_date = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.title
