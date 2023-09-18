from django.contrib import admin

# Register your models here.
from .models import Code,Coder
admin.site.register(Coder)
admin.site.register(Code)