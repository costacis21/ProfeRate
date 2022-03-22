from django.contrib import admin

# Register your models here.

from .models import Modules,Ratings,Profs
admin.site.register(Profs)
admin.site.register(Modules)
admin.site.register(Ratings)