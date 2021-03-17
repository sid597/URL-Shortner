from shortner import app
from api.routes import convert_to_base64
import unittest

conversion_list = [(1, 'b'),(2,'c'),(25,'z'),(100000, 'yAG'),(10000000,'MjAa')]

class TestUrlShortner(unittest.TestCase):
    


    def test_base10_to_base64_conversion(self):
        for p1, p2 in conversion_list:
            with self.subTest():
                self.assertEqual(convert_to_base64(p1),p2)
    
    def test0_shortner(self):
        request = app.test_client(self)
        response = request.post('/shorten/', json={
            "url": "https://github.com/sid597/infracloud"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['shortned_url'], 'http://127.0.0.1:5000/b')
        
    def test1_shortned_to_original_url(self):
        request = app.test_client(self) 
        response = request.get('/b')
        self.assertEqual(response.location, "https://github.com/sid597/infracloud")

if __name__ == '__main__':
    unittest.main()
