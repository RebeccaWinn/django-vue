from rest_framework import serializers
from .models import CalendarEvents,Reminders


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalendarEvents
        fields = '__all__'
        
class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model= Reminders
        fields = '__all__'