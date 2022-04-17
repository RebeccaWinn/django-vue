from django.urls import path

from . views import EventsView, RemindersView,ScrapingView,PostsView


urlpatterns = [
    path('events/', EventsView.as_view()),
    path('events/<int:id>', EventsView.as_view()),
    path('reminders/', RemindersView.as_view()),
    path('reminders/<int:id>', RemindersView.as_view()),
    path('scraping/', ScrapingView.as_view()),
    path('posts/', PostsView.as_view()),
    path('posts/<int:id>', PostsView.as_view()),



]
