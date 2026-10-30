import unittest

from app.app import app

class TestSafeRelease(unittest.TestCase):
    def setUp(self):
        self.client=app.test_client()

    def test_home_page(self):
        response=self.client.get("/")
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.get_data(as_text=True),"SafeRelease Application is Running!!")

    def test_Healthy_page(self):
        response=self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(),{"status": "Healthy"})

    if __name__=="__main__":
     unittest.main()
