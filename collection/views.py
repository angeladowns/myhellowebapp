from django.shortcuts import render
from collection.models import Film

# Create your views here.
def index(request):
    films = Film.objects.all()
    return render(request, 'index.html', {
    'films': films,
    })

def film_detail(request, slug):
    film = Film.objects.get(slug=slug)
    return render(request, 'films/film_detail.html', {
        'film': film,
    })
