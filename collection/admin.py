from django.contrib import admin

# import your model
from collection.models import Film

# set up automated slug creation
class FilmAdmin(admin.ModelAdmin):
    model = Film
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Film, FilmAdmin)
