import logging
from .assist_trip_service import AssistTripService
logger = logging.getLogger(__name__)


class QuotationService(object):

    @classmethod
    def define_quotation_coverages(cls):
        """ Return the desired quotation list.
            As the quotation endpoint itself filters the national or international coverages,
            the action is not necessary here"""
        # TODO: Maybe this would be better on the view itself?? A config file?
        return 1, 2, 20

    @classmethod
    def get_quotations(cls, data: dict):
        request_body = {'destination': int(data.get('selected_destination')),
                        'coverage_begin': data.get('boarding'),
                        'coverage_end': data.get('landing'),
                        'coverages': cls.define_quotation_coverages()}

        return AssistTripService.get_quotations(request_body)

    @staticmethod
    def map_product_to_quotation(quotation, product_list):
        desired_product_wrapper = [product for product in product_list if product.get("id") == quotation.get("product_id")]
        quotation["product"] = desired_product_wrapper[0]
