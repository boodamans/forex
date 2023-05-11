from app import app
from unittest import TestCase

class forextests(TestCase):
    def test_200(self):
       with app.test_client() as client:
        res = client.get('/')
        html = res.get_data(as_text=True)
        self.assertEqual(res.status_code, 200)

    def test_convert(self):
       with app.test_client() as client:
        res = client.post('/convert', data={
          'from': 'USD', 'to': 'USD', 'amount': 1
        }, follow_redirects=True)
        html = res.get_data(as_text=True)
        self.assertIn('Result = 1 USD', html)
