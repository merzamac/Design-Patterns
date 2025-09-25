from structural.Adapter.handlers import CsvDataHandler, JsonDataHandler


class CsvToJsonAdapter:
    def __init__(self, handler: CsvDataHandler):
        self.handler = handler

    def load_data(self, file_path):
        csv_data = self.handler.load_data(file_path)
        result = [dict(row) for row in csv_data]
        return result
