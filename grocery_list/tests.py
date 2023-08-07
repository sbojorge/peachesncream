from django.test import TestCase
from .models import Grocery
from django.contrib.auth.models import User


class TestViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='ella',
                                             password='rabbit')
        login = self.client.login(username='ella', password='rabbit')

    def test_authenticated_user_can_add_list(self):
        """
        Test authenticated user can create a shopping list
        """
        grocery = Grocery.objects.create(name='salad', item='tomates')
        response = self.client.post('/grocery_list/')
        self.assertEqual(response.status_code, 201)
        self.assertTemplateUsed(response, 'grocery_list/add_list.html')
