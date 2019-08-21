import logging
from collections import namedtuple

from .assist_trip_service import AssistTripService

logger = logging.getLogger(__name__)


class QuotationService(object):
    QuotationDTO = namedtuple('QuotationDTO',
                              ['id', 'name', 'baggage_damage_coverage', 'medic_expenses_coverage', 'max_age', 'min_age',
                               'elder_age', 'net_price', 'elder_net_price'])

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

    @classmethod
    def map_product_to_quotation(cls, quotation, product_list):
        desired_product_wrapper = [product for product in product_list if
                                   product.get("id") == quotation.get("product_id")]
        quotation["product"] = desired_product_wrapper[0]

    @classmethod
    def get_prices_in_brl(cls, quotation: dict) -> tuple:
        exchange_rate = quotation.get('exchange_rate')
        price = str(quotation.get('net_price') * exchange_rate).replace('.', ',')
        elder_price = str(quotation.get('elder_net_price') * exchange_rate).replace('.', ',')
        return price, elder_price

    @classmethod
    def map_to_dto(cls, quotation: dict, product_list: list, client_info: dict) -> dict:
        desired_product = [product for product in product_list if product.get("id") == quotation.get("product_id")][0]
        prices_tuple = cls.get_prices_in_brl(quotation)
        # TODO: Remove hardcodeds
        return {"id": quotation.get('product_id'), "name": quotation.get('product_name'), "net_price": prices_tuple[0],
                "elder_net_price": prices_tuple[1], "baggage_damage_coverage": cls.get_coverage_value(quotation, (20,)),
                "medic_expenses_coverage": cls.get_coverage_value(quotation, (1, 2)),
                "elder_age": desired_product.get('elder_age'), "max_age": desired_product.get('max_age'),
                "min_age": desired_product.get('min_age'), "client_info": client_info,
                "csrfmiddlewaretoken": client_info.get('csrfmiddlewaretoken')}

    @classmethod
    def get_coverage_value(cls, quotation, coverage_ids: tuple):
        coverage_wrapper = [coverage for coverage in quotation.get('coverages') if
                            coverage.get('coverage_id') in coverage_ids]
        if coverage_wrapper:
            return str(coverage_wrapper[0].get('currency')) + ' ' + str(coverage_wrapper[0].get('coverage_value'))
        return "-"
