import logging
from .assist_trip_service import AssistTripService
logger = logging.getLogger(__name__)

class QuotationService(object):

    @staticmethod
    def is_national(destination_id):
        """ Check if the destination is national (Brasil)"""
        # TODO: Remove harcoded verification, but how?
        return int(destination_id) == 1

    @classmethod
    def define_quotation_coverages(cls, selected_destination_id: int):
        """ Return the desired quotation list"""
        # TODO: Maybe this would be better on the view itself??
        if cls.is_national(selected_destination_id):
            return 1, 20
        return 2, 20

    @classmethod
    def get_quotations(cls, data: dict):
        request_body = {'destination': int(data.get('selected_destination')),
                        'coverage_begin': data.get('boarding'),
                        'coverage_end': data.get('landing'),
                        'coverages': cls.define_quotation_coverages(data.get('selected_destination'))}

        return AssistTripService.get_quotations(request_body)
