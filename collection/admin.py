from django.contrib import admin

# import your model
from collection.models import Film, Social

# set up automated slug creation
class FilmAdmin(admin.ModelAdmin):
    model = Film
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

class SocialAdmin(admin.ModelAdmin):
    model = Social
    list_display = ('network', 'username',)

# register
admin.site.register(Film, FilmAdmin)
admin.site.register(Social, SocialAdmin)
