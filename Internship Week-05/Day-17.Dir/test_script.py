
import unittest
from original_script import fetch_data_from_api, extract_currency_info

class TestCurrencyAPI(unittest.TestCase):

    def test_fetch_data_success(self):
        url = "https://api.exchangerate-api.com/v4/latest/USD"
        data = fetch_data_from_api(url)
        self.assertIsNotNone(data)
        self.assertIn("rates", data)

    def test_extract_currency_info_valid(self):
        dummy_json = {
            "base": "USD",
            "date": "2024-01-01",
            "rates": {
                "EUR": 0.85, "GBP": 0.75, "PKR": 280.0, "INR": 74.0,
                "JPY": 110.0, "CAD": 1.25, "AUD": 1.35
            }
        }
        base, date, filtered = extract_currency_info(dummy_json)
        self.assertEqual(base, "USD")
        self.assertEqual(date, "2024-01-01")
        self.assertEqual(len(filtered), 7)

    def test_extract_currency_info_missing_rates(self):
        dummy_json = {
            "base": "USD",
            "date": "2024-01-01",
            "rates": {}
        }
        base, date, filtered = extract_currency_info(dummy_json)
        self.assertEqual(filtered, {})

if __name__ == '__main__':
    unittest.main()






