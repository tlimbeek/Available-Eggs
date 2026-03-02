import unittest
import app as app_module


class TestAvailableEggs(unittest.TestCase):
    def setUp(self):
        self.client = app_module.app.test_client()

    def test_healthz(self):
        response = self.client.get('/healthz')
        self.assertEqual(response.status_code, 200)

    def test_exportcsv_status_and_content_type(self):
        response = self.client.get('/exportcsv')
        self.assertEqual(response.status_code, 200)
        self.assertIn('text/csv', response.content_type)

    def test_exportcsv_has_header_row(self):
        response = self.client.get('/exportcsv')
        text = response.data.decode('utf-8')
        self.assertIn('farm_name', text)
        self.assertIn('egg_type', text)

    def test_entries_returns_json_list(self):
        response = self.client.get('/entries')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        data = response.get_json()
        self.assertIsInstance(data, list)


if __name__ == '__main__':
    unittest.main()
