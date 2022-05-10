from django.contrib import admin
from .models import Bb, Rubric


class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'published', 'kind', 'rubric')
    list_display_links = ('title', 'kind', 'rubric')
    search_fields = ('title', 'description', 'kind')


admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)