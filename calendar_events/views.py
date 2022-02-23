from rest_framework.response import Response
from rest_framework import generics
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from . models import CalendarEvents, Reminders
from . serializers import EventSerializer, ReminderSerializer


class EventsView(generics.RetrieveAPIView):
    queryset = CalendarEvents.objects.all()

    def get(self, request,id=None):
        if id:
            item = CalendarEvents.objects.get(id=id)
            serializer = EventSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        queryset = CalendarEvents.objects.all()
        serializer = EventSerializer(queryset, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = EventSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id=None):
        item = CalendarEvents.objects.get(id=id)
        serializer = EventSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id=None):
        item = get_object_or_404(CalendarEvents, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})
    
class RemindersView(generics.RetrieveAPIView):
    def get(self, request,id=None):
        if id:
            item = Reminders.objects.get(id=id)
            serializer = ReminderSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        queryset = Reminders.objects.all()
        serializer = ReminderSerializer(queryset, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = ReminderSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id=None):
        item = Reminders.objects.get(id=id)
        serializer = ReminderSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id=None):
        item = get_object_or_404(Reminders, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})
    
    