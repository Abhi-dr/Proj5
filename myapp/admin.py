from django.contrib import admin
from .models import Note

# Register your models here.

admin.site.site_header = "Angaari Notes"

admin.site.register(Note)

