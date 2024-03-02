from django.contrib import admin

# Register your models here.
from .models import House, Topic


admin.site.register(House)
admin.site.register(Topic)