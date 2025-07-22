
import requests
import logging
from datetime import datetime

logging.basicConfig(filename='error_log.txt',
                    filemode='a',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def fetch_data_from_api(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        logging.info("Data fetched successfully from API.")
        return response.json()
    except requests.exceptions.RequestException as error:
        logging.error("API fetch failed: %s", error)
        return None


def extract_currency_info(json_data):
    try:
        base = json_data.get("base")
        date = json_data.get("date")
        rates = json_data.get("rates", {})

        selected = ["EUR", "GBP", "PKR", "INR", "JPY", "CAD", "AUD"]
        filtered_rates = {currency: rates[currency] for currency in selected if currency in rates}

        logging.info("Currency info extracted.")
        return base, date, filtered_rates
    except Exception as e:
        logging.error("Failed to extract currency info: %s", e)
        return None, None, {}


def display_and_save_report(base, date, currency_data, filename="exchange_report.txt"):
    try:
        report = f"Exchange Rate Summary\n---------------------\nBase: {base}\nDate: {date}\n\n"
        for currency, rate in currency_data.items():
            report += f"{currency}: {rate}\n"

        with open(filename, "w") as file:
            file.write(report)

        logging.info("Report saved to %s", filename)
        print(report)
    except Exception as e:
        logging.error("Failed to write report: %s", e)


if __name__ == "__main__":
    default_url = "https://api.exchangerate-api.com/v4/latest/USD"
    data = fetch_data_from_api(default_url)

    if data:
        base_currency, report_date, selected_rates = extract_currency_info(data)
        display_and_save_report(base_currency, report_date, selected_rates)
