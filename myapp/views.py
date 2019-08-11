from django.shortcuts import render
from django.http import HttpResponse

from .services.quotation_service import QuotationService
from .services.assist_trip_service import AssistTripService

# Create your views here.

def search(request):
    destination_list = AssistTripService.get_destinations()
    choices = sorted(destination_list, key=lambda dest: dest.get('id'))
    return render(request, 'myapp/search.html', {'dest_choices': choices})


def list(request):
    quotations = QuotationService.get_quotations(request.POST.dict())
    return HttpResponse(f"Still to implement {quotations}")


def buy(request):
    return HttpResponse(f"Still to implement {request.POST}")

