from django.shortcuts import render
from django.http import HttpResponse
import ast

from myapp.models import Purchase
from .services.quotation_service import QuotationService
from .services.assist_trip_service import AssistTripService


# Create your views here.
def search(request):
    destination_list = AssistTripService.get_destinations()
    choices = sorted(destination_list, key=lambda dest: dest.get('id'))
    return render(request, 'myapp/search.html', {'dest_choices': choices})


def list_quotations(request):
    client_info = request.POST.dict()
    quotations = QuotationService.get_quotations(client_info)
    product_list = AssistTripService.get_products()
    destination_list = AssistTripService.get_destinations()
    quotation_dto_list = []
    for quotation in quotations:
        quotation_dto_list.append(QuotationService.map_to_dto(quotation, product_list, client_info, destination_list))
    return render(request, 'myapp/list.html', {"quotation_list": quotation_dto_list})



#TODO: save the purchase action on the database!
#TODO: convert post_body to Purchase object
def purchase(request):
    post_body = ast.literal_eval(request.body.decode("utf-8"))
    # Sale.objects.create(product_id= )
    return HttpResponse(status=200)
