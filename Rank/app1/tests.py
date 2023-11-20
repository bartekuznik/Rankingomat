from django.test import TestCase
from .models import CustomUser, Rank

# Create your tests here.
class SingalTest(TestCase):
    def test_user(self):
        cusromuser = CustomUser(
            email = "user1223@b.com",
            username = "User",
            password = "123ascd."
        )
        cusromuser.save()

        self.assertTrue(
            hasattr(cusromuser, 'rank')
        )