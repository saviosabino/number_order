"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from order.models import Order
import random

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class OrderTest(TestCase):
    def setUp(self):
        MAX = 5
        self.alist = []
        for i in range(MAX):
            self.alist.append(random.randint(0,MAX))
        self.order = Order(self.alist)

    def show(self,res):
        self.assertEqual(1,1)
        print('media: ' + str(self.order.calcMedia()))
        print('listNord:' + str(self.alist))
        print('listOrd:' + str(res))

    def test_quicksort(self):
        self.show(self.order.quicksort())

    def test_bubblesort(self):
        self.show(self.order.bubblesort())

    def test_pythonsort(self):
        self.show(self.order.pythonsort())


