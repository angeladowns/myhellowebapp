from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify

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

@login_required
def edit_film(request, slug):
    film = Film.objects.get(slug=slug)

    if film.user != request.user:
        raise Http404

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

def create_film(request):
    form_class = FilmForm

    if request.method == 'POST':

        form = form_class(request.POST)
        if form.is_valid():
            film = form.save(commit=False)
            film.user = request.user
            film.slug = slugify(film.name)
            film.save()

            return redirect('film_detail', slug=film.slug)

    else:
        form = form_class()

    return render(request, 'films/create_film.html', {
            'form': form,
    })

def browse_by_name(request, initial=None):
    if initial:
        films = Film.objects.filter(
            name__istartswith=initial).order_by('name')
    else:
        films = Film.objects.all().order_by('name')

    return render(request, 'search/search.html', {
        'films': films,
        'initial': initial,
    })
