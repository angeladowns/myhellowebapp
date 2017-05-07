from django.shortcuts import render, redirect
from collection.forms import FilmForm
from collection.models import Film

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

def edit_film(request, slug):
    film = Film.objects.get(slug=slug)
    form_class = FilmForm
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=film)
        if form.is_valid():
            form.save()
            return redirect('film_detail', slug=film.slug)
        else:
            form = form_class(instance=film)
            return render(request, 'films/edit_film.html', {
                'film': film,
                'form': form,
            })
