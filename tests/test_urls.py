from django.test import TestCase


class TestUrls(TestCase):

    def test_Reservation_view_url_exists_at_desired_location(self):
        response = self.client.get('/reservations/')
        self.assertEqual(response.status_code, 200)