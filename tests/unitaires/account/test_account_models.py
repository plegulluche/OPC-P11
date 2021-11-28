import pytest

from django.test import Client
from account.models import Account

@pytest.mark.django_db
def test_Account_user_model():
    client = Client()
    new_user = Account.objects.create(username = 'blob',
                           email = 'blob@blobmail.com',
                           password = 'SuperPass1234')
    
    expected_value = "blob@blobmail.com"
    assert str(new_user.email) == expected_value
    assert new_user.is_admin == False 
    
    assert new_user.__str__() == new_user.email

