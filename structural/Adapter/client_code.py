from pathlib import Path

from structural.Adapter.adapters import CsvToJsonAdapter
from structural.Adapter.handlers import CsvDataHandler, JsonDataHandler


def client_code(data_handler, file_path):
    data = data_handler.load_data(file_path)
    print(f"{type(data_handler)} Data:", data, sep="\n")


def adapter():
    # Using CsvDataHandler with CsvToJsonAdapter
    csv_file_path = "structural/Adapter/data/sample_data.csv"
    csv_to_json_adapter = CsvToJsonAdapter(CsvDataHandler())
    client_code(csv_to_json_adapter, csv_file_path)
