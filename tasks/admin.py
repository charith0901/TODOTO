from django.contrib import admin
from .models import Task  # Import your Task model

admin.site.register(Task)  # Register Task model in Django Admin
