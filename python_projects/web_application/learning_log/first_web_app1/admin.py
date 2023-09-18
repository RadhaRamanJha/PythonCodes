from django.contrib import admin

# Register your models here.

# importing models created
from .models import Events,Entry

# registring models created on the site
admin.site.register(Events)
admin.site.register(Entry)