from django.test import TestCase
from .models import Book, Author
from django.contrib.auth.models import User
from decimal import *
from django.urls import reverse


class StoreViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='chakri', email='chakrikata@gmail.com', password='prabavathi*66'
        )
        author = Author.objects.create(first_name="stephen", last_name='King')
        book = Book.objects.create(title='Cujo', author=author, description='Darn scary', price='9.99', stock=1)

    def test_index(self):
        resp = self.client.get('/store/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('books' in resp.context)
        self.assertTrue(resp.context['books'].count()>0)
        print(resp.context)

    def test_cart(self):
        resp = self.client.get('/store/cart/')
        #self.assertEqual(resp.status_code, 302)

    def test_book_detail(self):
        resp = self.client.get('/store/book/1/')
        self.assertEqual(resp.status_code, 200)
        #self.assertEqual(resp.context['book'].pk, 1)
        #self.assertEqual(resp.context['book'].title, "Cujo")

    def test_add_to_cart(self):
        self.logged_in = self.client.login(username='chakri', password='prabavathi*66')
        self.assertTrue(self.logged_in)
        resp = self.client.get('/store/add/1/')
        resp = self.client.get('/store/cart/1/')
        #self.assertEqual(resp.context['total'], Decimal('9.99'))
        #self.assertEqual(resp.context['count'], 1)
       # self.assertEqual(resp.context['cart'].count(), 1)
        #self.assertEqual(resp.context['cart'].get().quantity, 1)