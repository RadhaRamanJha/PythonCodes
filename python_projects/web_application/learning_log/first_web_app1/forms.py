from django import forms
from .models import Events, Entry

class EventsForm(forms.ModelForm):
    """create new event"""
    class Meta:
        model = Events
        fields = ['event']
        labels = {'event':''}
    
class EntryForm(forms.ModelForm):
    """Creates entry for each event"""
    class Meta:
        model = Entry
        fields = ['entry']
        labels = {'entry':'Entry:'}
        widgets = {'entry': forms.Textarea(attrs={'cols':'20', 'rows':'10'})}
    