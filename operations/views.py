from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

#def index(request):
  #  return HttpResponse("Hello, world. You're at the operations index.")
def index(request):
    return render(request, 'inv/index.html')

def display_operation(request):
    items = Operation.objects.all()
    context = {
        'items': items,
        'header': 'Operation',
    }
    return render(request, 'inv/operation.html', context)

def display_mouvement(request):
    items = Mouvement.objects.all()
    context = {
        'items': items,
        'header': 'Mouvements',
    }
    return render(request, 'inv/mouvement.html', context)


def add_op(request, cls):
    if request.method == "POST":
        form = cls(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls()
        return render(request, 'inv/add_new.html', {'form' : form})

def add_operation(request):
        return add_op(request, operationsForm)