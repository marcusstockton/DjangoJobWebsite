import datetime
from django.test import TestCase
from Address.models import Address, AddressType
from Company.models import Company


class CompanyTestCase(TestCase):
    def setUp(self):
        addressType1 = AddressType.objects.create(description="Residential", is_active=True)
        addressType2 = AddressType.objects.create(description="Business", is_active=True)
        address1 = Address.objects.create(address_line_1="Address1", address_line_2="address2", post_code="EX1EX1", county="Devon", country="UK", address_type=addressType1)
        address2 = Address.objects.create(address_line_1="Blah blah", address_line_2="some guff", post_code="TQ1TQ1", county="Devon", country="UK", address_type=addressType2)
        company1 = Company.objects.create(company_name = "Test Company One", address=address1)
        company2 = Company.objects.create(company_name = "Test Company Two", address=address2)

    def test_company_created_sucessfully(self):
        company1 = Company.objects.get(company_name='Test Company One')
        company2 = Company.objects.get(company_name='Test Company Two')
        self.assertTrue(company1.address.address_line_1 == 'Address1', "Company 1's address line 1 is {0} instead of {1}".format(
            company1.address.address_line_1, 'Address1'))  # only displays msg on failure
        self.assertIsNotNone(company2)

    def tearDown(self):
        # Clear down the data.
        address1 = Address.objects.get(address_line_1='Address1')
        address2 = Address.objects.get(address_line_1='Blah blah')
        company1 = Company.objects.get(company_name="Test Company One")
        company2 = Company.objects.get(company_name="Test Company Two")

        address1.delete()
        address2.delete()
        company1.delete()
        company2.delete()