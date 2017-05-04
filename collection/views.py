from django.shortcuts import render

# Create your views here.
def index(request):
    # defining the variable
    number = 6
    thing = "Thing name"
    # this is your new view
    return render(request, 'index.html', {
    'number': number,
    'thing': thing,
    })
