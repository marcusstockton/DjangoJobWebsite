from django.test import TestCase, Client
from .models import User

# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username="mstockton", email='mstockton@test.com', password='12345')
        User.objects.create_user(username="Test", email='test@test.com', password='12345')
        
    def test_users_can_log_in(self):
        c = Client()
        c.login(username='mstockton', password='12345')
        response = c.get('/')
        self.assertEqual(str(response.context['user']), 'mstockton')