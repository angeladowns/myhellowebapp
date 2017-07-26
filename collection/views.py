from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context

from collection.forms import FilmForm
from collection.forms import ContactForm
from collection.models import Film

def index(request):
    films = Film.objects.all()
    return render(request, 'index.html', {
        'films': films,
    })

def film_detail(request, slug):
    film = Film.objects.get(slug=slug)
    # grab all the objects social media accounts
    social_accounts = film.social_accounts.all()
    # pass it to the template
    return render(request, 'films/film_detail.html', {
        'film': film,
        'social_accounts': social_accounts,
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

def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            form_content = form.cleaned_data['content']

            # email the profile with the contact info
            template = get_template('contact_template.txt')

            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content = template.render(context)

            email = EmailMessage(
                'New contact form submission',
                content,
                'Your website <angela@website.com>',
                ['angela@myemailaddress.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('contact')

    return render(request, 'contact.html', {
        'form': form_class,
    })
