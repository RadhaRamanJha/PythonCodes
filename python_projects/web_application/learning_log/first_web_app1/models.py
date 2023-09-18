from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Events(models.Model):
    """Events that ocuured today"""
    event = models.CharField(max_length=300)
    time_field = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Events'

    def __str__(self):
        return(str(self.event))
    
class Entry(models.Model):
    """Description of Events"""
    event = models.ForeignKey(Events, on_delete = models.CASCADE)
    # (default='') was added because paramaeter of model can be left empty
    entry = models.TextField(default='')
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self) :
        """Return a string representation of model"""
        return f"{self.entry[:10]}..."