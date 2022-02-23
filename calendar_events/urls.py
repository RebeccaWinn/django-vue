from django.urls import path
from . views import EventsView, RemindersView


urlpatterns = [
    path('events/', EventsView.as_view()),
    path('events/<int:id>', EventsView.as_view()),
    path('reminders/', RemindersView.as_view()),
    path('reminders/<int:id>', RemindersView.as_view())


]
