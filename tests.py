import unittest

class PrimitiveTests(unittest.TestCase):
    def setUp(self):
        self.url = "https://jsonplaceholder.typicode.com/posts"


    def test_view_post(self):
        self.assertEqual(self.url.status_code, 200)


if __name__ == "__main__":
    unittest.main()
