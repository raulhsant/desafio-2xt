from django.shortcuts import render
from django.http import HttpResponse

from .services.quotation_service import QuotationService
from .services.assist_trip_service import AssistTripService

# Create your views here.

def search(request):
    destination_list = AssistTripService.get_destinations()
    choices = sorted(destination_list, key=lambda dest: dest.get('id'))
    return render(request, 'myapp/search.html', {'dest_choices': choices})

# TODO: mount the object as needed on the view to just show it there!
def list(request):
    quotation_list = QuotationService.get_quotations(request.POST.dict())
    product_list = AssistTripService.get_products()
    for quotation in quotation_list:
        QuotationService.map_product_to_quotation(quotation, product_list)
    print(quotation_list)
    return render(request, 'myapp/list.html', {"quotation_list": quotation_list, "product_list": product_list})


def buy(request):
    return HttpResponse(f"Still to implement {request.POST}")

