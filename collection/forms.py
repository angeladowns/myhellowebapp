from django.forms import ModelForm
from collection.models import Film


class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ('name', 'description',)
