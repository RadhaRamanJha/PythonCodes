from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

# importing Events and Entry from models
from .models import Events, Entry
# importing EventsForm from forms
from .forms import EventsForm, EntryForm

# Create your views here.
def index(request):
    """The home page for Learning first_web."""
    return render(request, 'first_web_app1/index.html')

@login_required
def events(request):
    """Shows all events"""
    events = Events.objects.filter(owner=request.user).order_by("time_field")
    context = {'events': events}
    return render(request, 'first_web_app1/events.html',context)

@login_required
def event(request, event_id):
    """Shows a single event and all its entries."""
    event = Events.objects.get(id=event_id)
    # Making sure the topic belongs to the current user
    if event.owner != request.user:
        raise Http404
    entries = event.entry_set.order_by('-date_added')
    context = {'event':event, 'entries': entries}
    return render(request, 'first_web_app1/event.html', context)

@login_required
def new_event(request):
    """Add a new event"""
    if request.method != 'POST':
        # no data submitted; create a blank form.
        form = EventsForm()
    else:
        # post the data submitted, process the data
        form = EventsForm(data=request.POST)
        if form.is_valid():
            new_event = form.save(commit=False)
            new_event.owner = request.user
            new_event.save()
            return redirect('first_web_app1:events')
        
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'first_web_app1/new_event.html', context)

@login_required
def new_entry(request, event_id):
    """New entry given request and event_id"""
    event = Events.objects.get(id=event_id)

    if request.method != 'POST':
        # No data submitted create a blank entry form
        form = EntryForm()
    else:
        # Post the data submitted; process the data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.event = event
            new_entry.save()
            return redirect('first_web_app1:event', event_id=event_id)
        
    # Display a blank or invalid form.
    context = {'event': event, 'form': form} 
    # repeted mistake i always put 'topic' in place of 'event'
    # error which results is "Reverse for 'new_entry' with arguments '('',)' not found. 1 pattern(s) tried: ['new_entry/(?P<topic_id>[0-9]+)/$']"
    # as context is a dictionary the return function tries to display a form page based on key 'topic'
    # which is not present in my database hence getiing an error    
    return render(request, 'first_web_app1/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry"""
    entry = Entry.objects.get(id = entry_id)
    event = entry.event
    if event.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request so prefill the form with current entry
        form = EntryForm(instance=entry)
    else:
        # post the data submitted ; process data (save the data if valid)
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('first_web_app1:event', event_id = event.id)
        
    context = {'entry':entry , 'event':event, 'form':form}
    return(render(request,'first_web_app1/edit_entry.html',context))
    