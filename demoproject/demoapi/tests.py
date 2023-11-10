from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Data

# Create your tests here.
valid_data = {
        "sale_type": "Test Sale Type",
        "sold_date": "2023-11-11",
        "property_type": "Single Family Residential",
        "address": "82 W Spindle Tree Cir",
        "city": "The Woodlands",
        "state_or_province": "TX",
        "zip_or_postal_code": 77382,
        "price": 495000,
        "beds": 4,
        "baths": 3.5,
        "location": "Wdlnds Village Sterling Ridge",
        "square_feet": 2561,
        "lot_size": 7363,
        "year_built": 2007,
        "days_on_market": 1,
        "hoa_per_month": None,
        "status": "Active",
        "next_open_house_start_time": "June-24-2023 02:00 PM",
        "next_open_house_end_time": "June-24-2023 04:00 PM",
        "url": "https://www.redfin.com/TX/The-Woodlands/82-W-Spindle-Tree-Cir-77382/home/32642692",
        "source": "HARMLS",
        "mls_n0": 95940947,
        "favorite": "N",
        "interested": "Y",
        "latitude": 30.1760265,
        "longitude": -95.5873758
    }

invalid_data = {
        "sale_type": "Invalid Data Sale Type",
        "sold_date": "2023-11-11",
        "property_type": "Single Family Residential",
        "address": "82 W Spindle Tree Cir",
        "city": "The Woodlands",
        "state_or_province": "TX",
        "zip_or_postal_code": 77382,
        "price": 495000,
        "beds": 4,
        "baths": 3.5,
        "location": "Wdlnds Village Sterling Ridge",
        "square_feet": 2561,
        "lot_size": 7363,
        "year_built": 2007,
        "days_on_market": 1,
        "hoa_per_month": None,
        "status": "Active",
        "next_open_house_start_time": "A date",
        "next_open_house_end_time": "A date",
        "url": "bad url",
        "source": "HARMLS",
        "mls_n0": "95940947",
        "favorite": "N",
        "interested": "Y",
        "latitude": 30.1760265,
        "longitude": -95.5873758
    }
class ApiTest(TestCase):
    def setUp(self):
        # Create some test data
        self.client = APIClient()
        self.valid_input_data = valid_data
        self.invalid_input_data = invalid_data
        self.valid_data = Data.objects.create(**self.valid_input_data)

    def test_create_valid_data(self):
        response = self.client.post('/api/', self.valid_input_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_data(self):
        response = self.client.post('/api/', self.invalid_input_data, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_data_list(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_data(self):
        response = self.client.get(f'/api/{self.valid_data.id}', follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['sale_type'], 'Test Sale Type' )

    def test_update_single_data(self):
        updated_data = self.valid_input_data
        updated_data['sale_type'] = "updated sale type"
        response = self.client.put(f'/api/{self.valid_data.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['sale_type'], "updated sale type" )

    def test_delete_data(self):
        response = self.client.delete(f'/api/{self.valid_data.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Data.objects.count(), 0)

    def invalid_data_detail(self):
        response = self.client.get(f'/api/9999/')   #invalid ID - 9999
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
