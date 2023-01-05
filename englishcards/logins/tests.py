from django.test import TestCase
from .models import User
# Create your tests here.


class TestUserModel(TestCase):

    def test_if_users_inserted_same_name(self):
        self.user = User.objects.create(
            username = 'testuser',
            email = 'nowy@nowy.com',
            password = 'sadasda21.'
        )
        self.user2 = User.objects.create(
            username = 'testuser',
            email = 'nowy@nowy.com',
            password = 'sadasda21.'
        )
        self.assertIsNotNone(self.user)
        # self.assertIsNotNone(self.user2)
        
        
    def test_if_user_inserted(self):
        self.user = User.objects.create(
            username = 'testuser',
            email = 'nowy@nowy.com',
            password = 'sadasda21.'
        )
        self.assertIsNotNone(self.user)