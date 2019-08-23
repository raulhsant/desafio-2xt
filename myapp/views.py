from django.shortcuts import render
from django.http import HttpResponse
import ast
from datetime import datetime

from myapp.models import Purchase, Insured
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


def purchase(request):
    post_body = ast.literal_eval(request.body.decode("utf-8"))
    purchase_response = AssistTripService.make_purchase(post_body)
    if purchase_response.get("id"):
        _purchase = Purchase(id=purchase_response.get("id"))
        _purchase.save()
        for insured_dict in purchase_response.get("insureds"):
            insured = Insured()
            insured.assist_trip_id = insured_dict.get("id")
            insured.document_url = insured_dict.get("document_url")
            insured.policy_number = insured_dict.get("policy_number")
            insured.zurich_policy_number = insured_dict.get("zurich_policy_number")
            insured.travel_assistance_voucher = insured_dict.get("travel_assistance_voucher")
            insured.insurance_ticket = insured_dict.get("insurance_ticket")
            insured.purchase = _purchase
            insured.save()

        # Sale.objects.create(product_id= )
        return HttpResponse(status=200)
    return HttpResponse(status=400)  # Return bad request for whatever error?
