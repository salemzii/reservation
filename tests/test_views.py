from django.test import TestCase
from django.urls import reverse
from reservations.models import Rental, Reservations
from datetime import datetime



class ReservationViewTest(TestCase):


    @classmethod
    def setUpTestData(cls) -> None:
        rental = Rental.objects.create(name="rental-1")
        Reservations.objects.create(rental_id=rental, checkin=datetime(2022, 2, 23, 0, 0),
         checkout=datetime(2022, 2, 26, 0, 0))

    def test_reservations_view_accessible_by_name(self):
        response = self.client.get(reverse('reservations'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('reservations'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reservations.html')

    def test_view_returns_correct_context(self):
        #check the context dictionary to see if it returns expected results
        response = self.client.get(reverse('reservations'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['maps'])
        self.assertTrue(type(response.context['maps']) == list)
