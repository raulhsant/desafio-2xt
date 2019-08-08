from django.shortcuts import render
from django.http import HttpResponse
from.forms import SearchForm


# Create your views here.


def search(request):

    return render(request, 'myapp/search.html', {'form': SearchForm})


def list(request):
    return HttpResponse(f"Still to implement {request.POST}")


def buy(request):
    return HttpResponse(f"Still to implement {request.POST}")

