from django.shortcuts import render
from django.http import HttpResponse
from.forms import SearchForm

from .services.quotation_service import QuotationService


# Create your views here.


def search(request):
    return render(request, 'myapp/search.html', {'form': SearchForm})


def list(request):
    quotations = QuotationService.get_quotations(request.POST.dict())
    return HttpResponse(f"Still to implement {quotations}")


def buy(request):
    return HttpResponse(f"Still to implement {request.POST}")

