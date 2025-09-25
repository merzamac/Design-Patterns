import csv
import json
from unittest import result

from structural.Adapter.client_interface import Data


class JsonDataHandler(Data):
    def load_data(self, file_path):
        with open(file_path, "r") as file:
            return json.load(file)


class CsvDataHandler(Data):
    def load_data(self, file_path):
        with open(file_path, newline="") as file:
            return list(csv.DictReader(file))
