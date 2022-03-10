from datetime import date
from django.db import models
from django.urls import reverse




class CalendarEvents(models.Model):
    name = models.CharField(max_length=255)
    start = models.CharField(max_length=255)
    end = models.CharField(max_length=255)

    
    def __str__(self):
        return self.name 
class Meta:
    ordering=('name',)
    # def get_absolute_url(self):
    #     return reverse ('calendar-details',kwargs={'pk': self.pk})    
    
    
    
class Reminders(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name 
    
    # def get_absolute_url(self):
    #     return reverse ('reminder-details',kwargs={'pk': self.pk})    
