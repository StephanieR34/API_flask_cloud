import unittest
import app


class TestApi(unittest.TestCase):
    # check response status is 200
    def test_latest_by_country_status(self):
        tester = app.app.test_client(self)
        response = tester.get("/latest_by_country/Bulgaria")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    # check the response content
    def test_latest_by_country_type(self):
        tester = app.app.test_client(self)
        response = tester.get("/latest_by_country/Bulgaria")
        self.assertEqual(response.content_type, "application/json")

    # check the response DATA
    def test_latest_by_country_data(self):
        tester = app.app.test_client(self)
        response = tester.get("/latest_by_country/Bulgaria")
        self.assertTrue(b'Year' in response.data)

    # check response status is 200
    def test_average_by_year_status(self):
        tester = app.app.test_client(self)
        response = tester.get("/average_by_year/2017")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    # check the response content
    def test_average_by_year_type(self):
        tester = app.app.test_client(self)
        response = tester.get("/average_by_year/2017")
        self.assertEqual(response.content_type, "application/json")

    # check the response DATA
    def test_average_by_year_data(self):
        tester = app.app.test_client(self)
        response = tester.get("/average_by_year/2017")
        self.assertTrue(b'Total' in response.data)


if __name__ == '__main__':
    unittest.main()