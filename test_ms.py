import unittest
import requests

class TestMicroservice(unittest.TestCase):

    def test_validate_email_valid(self):
        url = 'http://localhost:5000/validate-email'
        data = {'email': 'test@example.com'}
        response = requests.post(url, json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['is_valid'], True)

    def test_validate_email_invalid(self):
        url = 'http://localhost:5000/validate-email'
        data = {'email': 'invalid-email'}
        response = requests.post(url, json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['is_valid'], False)

if __name__ == '__main__':
    unittest.main()
