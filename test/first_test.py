from datetime import datetime
import pytest
from products.models import Product
from django.test import Client
from pytest_django.asserts import assertTemplateUsed
pytestmark = pytest.mark.django_db


class TestProductModel:

    def test_save(db):
        now = datetime.now()
        print(str(now))
        product = Product.objects.create(
            name="Sample product",
            description="Lorem ipsum",
            price=152.99,
            photo="test",
            publish_date=now)

        assert product.name == 'Sample product'
        assert product.price == 152.99
        assert product.publish_date == now

    def test_template_sign_in(db):
        client = Client()
        response = client.get('/accounts/login/')
        assertTemplateUsed(response, 'registration/login.html')
