"""Defines the URL patterns for first_web_app1"""

from django.urls import path

from .import views

app_name = 'first_web_app1'

urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
    # page that shows all events
    path('events/', views.events, name='events'),
    # Detail page for a single event
    path('events/<int:event_id>/', views.event, name='event'),
    # Page for adding a new event
    path('new_event/', views.new_event, name='new_event'),
    # Page for adding new entry
    path('new_entry/<int:event_id>/', views.new_entry, name='new_entry'),
    # Page for editing entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry')
]