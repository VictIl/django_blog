from django.contrib import admin

 

from .models import *

class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','quote', 'time_created', 'img', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title','quote', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_created')

class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'scale')
    list_display_links = ('id', 'scale')
    search_fields = ('scale',)


admin.site.register(Post)

admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating, RatingAdmin)
