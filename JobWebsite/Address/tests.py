from django.core.exceptions import ValidationError
from django.db import connection, IntegrityError, transaction
from django.test import TestCase, Client
from django.test.utils import override_settings

from .forms import AddressForm
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

class AddressFormTestCase(TestCase):
    """ Test the address form """
    @override_settings(DEBUG=True)
    def setUp(self):
        user = User.objects.create_user(
            username="mstockton", 
            email='mstockton@test.com', 
            password='12345')
        Address.objects.create(
            address_type=AddressType.objects.create(
                description="Business", 
                is_active=True), 
            address_line_1='Address Line 1',
            post_code="EX11EX", 
            county="Devon", 
            country="GB"
            )

    def test_address_form_init(self):
        form = AddressForm()
        self.assertFalse(form.is_valid())

    def test_cleaned_data(self):
        address_type = AddressType.objects.get(description='Business')
        address = Address.objects.get(post_code="EX11EX")
        self.assertIsNotNone(address_type)
        self.assertIsNotNone(address)
        form = AddressForm(data={
            'address_type': address_type.id, 
            'address_line_1': address.address_line_1, 
            'post_code':address.post_code, 
            'county': address.county, 
            'country': address.country})
            
        self.assertTrue(form.is_bound)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.clean_address_line_1(),'Address Line 1')
        self.assertEqual(form.clean_post_code(),'EX11EX')
        self.assertEqual(form.clean_county(),'Devon')
        self.assertEqual(form.clean_country(),'GB')