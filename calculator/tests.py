from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Tip

class TipAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.tip_data = {'bill_amount': '100.00', 'tip_percentage': '15.00'}
        self.tip = Tip.objects.create(bill_amount='50.00', tip_percentage='10.00', total_tip='5.00', total_amount='55.00')

    def test_tip_list_create_api(self):
        response = self.client.post('/api/tips/', self.tip_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_tip_retrieve_update_destroy_api(self):
        response = self.client.get(f'/api/tips/{self.tip.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        updated_data = {'bill_amount': '150.00', 'tip_percentage': '20.00'}
        response = self.client.put(f'/api/tips/{self.tip.id}/', updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.delete(f'/api/tips/{self.tip.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
