from django.shortcuts import render
from collection.models import Film

# Create your views here.
def index(request):
    films = Film.objects.all()
    return render(request, 'index.html', {
    'films': films,
    })
    # defining the variable
    number = 6
    thing = "Thing name"
    # this is your new view
    return render(request, 'index.html', {
        'number': number,
        'thing': thing,
    })
