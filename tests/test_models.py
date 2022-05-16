from datetime import datetime
from django.test import TestCase
from reservations.models import Rental, Reservations


class RentalModelTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        Rental.objects.create(name="rental-1")
    
    def test_name_label(self):
        rental = Rental.objects.get(id=1)
        name_label = rental._meta.get_field('name').verbose_name

        self.assertEqual(name_label, 'name')


class ReservationsModelTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        rental = Rental.objects.create(name="rental-1")
        Reservations.objects.create(rental_id=rental, checkin=datetime(2022, 2, 23, 0, 0),
         checkout=datetime(2022, 2, 26, 0, 0))
    
    def test_rental_id_name_label(self):
        resv = Reservations.objects.get(id=1)
        label = resv._meta.get_field('rental_id').verbose_name

        self.assertEqual(label, 'rental id')
    
    def test_checkin_name_label(self):
        resv = Reservations.objects.get(id=1)
        label = resv._meta.get_field('checkin').verbose_name

        self.assertEqual(label, 'checkin')

    def test_checkout_name_label(self):
        resv = Reservations.objects.get(id=1)
        label = resv._meta.get_field('checkout').verbose_name

        self.assertEqual(label, 'checkout')