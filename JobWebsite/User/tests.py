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
        User.objects.create_user(username="mstockton",
                                 email='mstockton@test.com', password='12345')
        User.objects.create_user(
            username="Test", email='test@test.com', password='12345')
        # show_sql()


    def test_users_can_log_in(self):
        c = Client()
        c.login(username='mstockton', password='12345')
        response = c.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.context['user']), 'mstockton')
        # show_sql()


    def test_user_can_log_out(self):
        # Write tests in here
        c = Client()
        c.logout()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.context['user']), 'AnonymousUser')
        # show_sql()


    def test_invalid_login_details_returns_errors(self):
        c = Client()
        response = c.post('/login/', {'username': 'john', 'password': 'doe'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Your username and password didn\'t match. Please try again.", response.content)


    def test_empty_login_details_returns_errors(self):
        c = Client()
        response = c.post('/login/', {'username': '', 'password': ''})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<p id="error_1_id_username" class="invalid-feedback"><strong>This field is required.</strong></p>', response.content)
        self.assertIn(b'<p id="error_1_id_password" class="invalid-feedback"><strong>This field is required.</strong></p', response.content)


    def test_error_when_creating_user_with_invalid_data(self):
        User.objects.create_user(username="failingUser")
        user = User.objects.get(username="failingUser")
        # If no password is provided, set_unusable_password() will be called.
        # has_usable_password()
        # Returns False if set_unusable_password() has been called for this user.
        self.assertFalse(user.has_usable_password())