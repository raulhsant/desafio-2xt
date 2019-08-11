from collections import namedtuple

import requests
import base64
import logging
import json
from .config import user, passw, base_uri

logger = logging.getLogger(__name__)


def get_string(obfuscated_value):
    return base64.b64decode(obfuscated_value).decode('utf-8')


class AssistTripService(object):

    @staticmethod
    def __get_destinations_uri():
        return f"{base_uri}/base/destinations"

    @staticmethod
    def __get_products_uri():
        return f"{base_uri}/base/products"

    @staticmethod
    def __get_quotation_uri():
        return f"{base_uri}/quotation"

    @staticmethod
    def __get_purchase_uri():
        return f"{base_uri}/purchase"

    @staticmethod
    def __get_cancel_purchase_uri(purchase_id):
        return f"{base_uri}/purchase/{purchase_id}/cancel"

    @staticmethod
    def basic_auth_get_request(uri):
        response = requests.get(uri, auth=(get_string(user), get_string(passw)))
        if response.status_code != 200:
            logger.error(uri)
            logger.error(response)
             # should I treat this or just return empty?
            return {}
        else:
            return response.json()

    @staticmethod
    def basic_auth_post_request(uri: str, body: dict):

        response = requests.post(uri, auth=(get_string(user), get_string(passw)), data=json.dumps(body))
        if response.status_code != 200:
            logger.error(uri)
            logger.error(response)
             # should I treat this or just return empty?
            return {}
        else:
            return response.json()


    @staticmethod
    def get_destinations():
        uri = AssistTripService.__get_destinations_uri()
        return AssistTripService.basic_auth_get_request(uri)
        # Returning mock due to assist trip down time
        # return [{"id": 1,"name": "Brasil"}]

    @classmethod
    def get_quotations(cls, request_body):
        uri = cls.__get_quotation_uri()
        response = cls.basic_auth_post_request(uri, request_body)
        return response
