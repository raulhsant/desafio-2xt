from collections import namedtuple

import requests
import base64
import logging
from .config import user, passw, base_uri

logger = logging.getLogger(__name__)


def get_string(obfuscated_value):
    return base64.b64decode(obfuscated_value).decode('utf-8')


class AssistTripService(object):

    @staticmethod
    def get_destinations_uri():
        return f"{base_uri}/base/destinations"

    @staticmethod
    def get_products_uri():
        return f"{base_uri}/base/products"

    @staticmethod
    def get_quotation_uri():
        return f"{base_uri}/quotation"

    @staticmethod
    def get_purchase_uri():
        return f"{base_uri}/purchase"

    @staticmethod
    def get_cancel_purchase_uri(purchase_id):
        return f"{base_uri}/purchase/{purchase_id}/cancel"

    @staticmethod
    def basic_auth_get_request(uri):
        result_list = []
        response = requests.get(uri, auth=(get_string(user), get_string(passw)))
        if response.status_code != 200:
            logger.error(uri)
            logger.error(response)
             # should I treat this or just return empty?
        else:
            response_dict = response.json()
            destination = namedtuple('Destination', 'id name')
            for item in response_dict:
                result_list.append(destination(item.get('id'), item.get('name')))
        return result_list


    @staticmethod
    def get_destinations():
        uri = AssistTripService.get_destinations_uri()
        return AssistTripService.basic_auth_get_request(uri)
