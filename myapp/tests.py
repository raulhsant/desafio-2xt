from django.test import TestCase
from myapp.services.quotation_service import QuotationService


# Create your tests here.

# TODO: Implement tests
class TestQuotationService(TestCase):
    def test_get_prices_in_brl_with_brl_price_assert_round(self):
        quotation = {
            'exchange_rate': 1,
            'net_price': 12,
            'elder_net_price': 20.758,
        }

        price_tuple = QuotationService.get_prices_in_brl(quotation)

        self.assertEquals("20,76", price_tuple[1])
        self.assertEquals("12,00", price_tuple[0])

    def test_get_prices_in_brl_with_exchange_price_assert_round(self):
        quotation = {
            'exchange_rate': 2,
            'net_price': 12,
            'elder_net_price': 20.758,
        }

        price_tuple = QuotationService.get_prices_in_brl(quotation)

        self.assertEquals("41,52", price_tuple[1])
        self.assertEquals("24,00", price_tuple[0])

    def test_get_prices_in_brl_without_exchange_return_0(self):
        quotation = {
            'exchange_rate': 0,
            'net_price': 12,
            'elder_net_price': 20.758,
        }

        price_tuple = QuotationService.get_prices_in_brl(quotation)

        self.assertEquals("0,00", price_tuple[1])
        self.assertEquals("0,00", price_tuple[0])
