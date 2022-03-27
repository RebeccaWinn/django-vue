from rest_framework import serializers
from .models import CalendarEvents,Reminders,ScrapingItem


class ScrapingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrapingItem
        fields = '__all__'
        

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalendarEvents
        fields = '__all__'
        
class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model= Reminders
        fields = '__all__'