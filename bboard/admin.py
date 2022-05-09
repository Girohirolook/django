from django.contrib import admin
from .models import Bb


class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'published', 'kind')
    list_display_links = ('title', 'kind')


admin.site.register(Bb, BbAdmin)
