from django.db import connection
from django.test import TestCase, Client
from django.test.utils import override_settings

from .models import User


def show_sql():
    for query in connection.queries:
        print(query['sql'])

class UserTestCase(TestCase):
    @override_settings(DEBUG=True)
    def setUp(self):
        User.objects.create_user(username="mstockton", email='mstockton@test.com', password='12345')
        User.objects.create_user(username="Test", email='test@test.com', password='12345')
        show_sql()
        
    def test_users_can_log_in(self):
        c = Client()
        c.login(username='mstockton', password='12345')
        response = c.get('/')
        self.assertEqual(str(response.context['user']), 'mstockton')
        show_sql()
