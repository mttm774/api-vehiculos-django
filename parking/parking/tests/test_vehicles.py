import json
from django.test import TestCase
from django.urls import reverse

from vehicle_management.models import vehicle

class test_vehicle(TestCase):

    @classmethod
    def setUpTestData(cls):
        mi_vehiculo=vehicle.objects.create(
            placa='iut123',
            marca='chevrolet',
            color_vehiculo=1,
            modelo=1990
        )

    def tearDown(self):
        pass

    def test_view_vehicle_list(self):
        response=self.client.get('/api/vehicle/list')
        data=json.loads(response.content.decode('utf-8'))
       
        self.assertEqual(response.status_code,200)
        self.assertGreater(len(data),0)

    def test_create_vehicle(self):
        response=self.client.post(
            '/api/vehicle/list',
            data={
                'placa':'wer123',
                'marca':'mazda',
                'color':'1',
                'modelo':'1990'
            }
        )
        self.assertIn(response.status_code, [200, 201])
        filtered_vehicle=vehicle.objects.filter(placa='wer123').first()
        self.assertEqual(filtered_vehicle.marca,'mazda')


    def test_update_vehicle(self):
        mi_vehiculo=vehicle.objects.create(
            placa='ucq123',
            marca='chevrolet',
            color_vehiculo=1,
            modelo=1990
        )
        valid_vehicle = {
            'placa': 'XYZ456',
            'marca': 'Honda',
            'color': 'Azul',
            'modelo': '1998'
        }
        url = reverse('actualizar_vehiculo', kwargs={'pkid': mi_vehiculo.id})
        valid_vehicle_json = json.dumps(valid_vehicle)
        response = self.client.put(url, valid_vehicle_json, content_type='application/json')
        self.assertIn(response.status_code, [200, 201])