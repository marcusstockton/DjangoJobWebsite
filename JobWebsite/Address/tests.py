from django.core.exceptions import ValidationError
from django.db import connection, IntegrityError, transaction
from django.test import TestCase, Client
from django.test.utils import override_settings

from .models import Address, AddressType
from User.models import User


class AddressTestCase(TestCase):
    """ Test Address functionality """
    @override_settings(DEBUG=True)
    def setUp(self):
        user = User.objects.create_user(
            username="mstockton", email='mstockton@test.com', password='12345')
        Address.objects.create(address_type=AddressType.objects.create(description="Business", is_active=True), address_line_1='Address Line 1',
                                address_line_2="Address Line 2", post_code="EX11EX", county="Devon", country="United Kingdom")

    def test_address_loads_correctly(self):
        """ Tests that addresses are correctly returned from the DB """
        address = Address.objects.all().first()
        self.assertEqual(address.address_line_1, "Address Line 1")

    def test_address_creation_fails_with_invalid_data(self):
        """ Tests that Integrety errors are thrown when trying to save invalid objects """
        self.assertRaises(IntegrityError, lambda: Address.objects.create(
            address_line_1="Address Line 1"))

    def test_validation_on_invalid_address(self):
        """ Tests that validation errors are thrown when updating an Address with invalid data """
        address = Address.objects.all().first()
        address.address_type = None
        self.assertRaises(ValidationError, lambda: address.full_clean())
