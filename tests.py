import unittest
import requests

class PrimitiveTests(unittest.TestCase):
    def setUp(self):
        self.url = "https://jsonplaceholder.typicode.com/posts"


    def test_view_post(self):
        self.resp = requests.get(self.url)
        self.assertEqual(self.resp.status_code, 200)

    def test_create_post(self):
        self.resp = requests.post(self.url)
        self.assertEqual(self.resp.status_code, 201)


if __name__ == "__main__":
    unittest.main()
