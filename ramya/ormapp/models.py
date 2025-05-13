from django.db import models
from django.contrib import admin
class Movie(models.Model):
    Name=models.CharField(max_length=50,primary_key=True)
    Actor=models.CharField(max_length=25)
    Language=models.CharField(max_length=20)
    Budget=models.IntegerField()
    Genre=models.CharField(max_length=20)
    ReleaseDate=models.DateField()
class MovieAdmin(admin.ModelAdmin):
    list_display=('Name','Actor','Language','Budget','Genre','ReleaseDate')