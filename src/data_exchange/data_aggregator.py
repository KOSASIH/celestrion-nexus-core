import json
import os
from datetime import datetime

class DataAggregator:
    def __init__(self, storage_path='data_storage'):
        self.storage_path = storage_path
        os.makedirs(self.storage_path, exist_ok=True)

    def aggregate_data(self, data):
        """Aggregates incoming data and stores it in a JSON file."""
        timestamp = datetime.utcnow().isoformat() + "Z"
        data_entry = {
            "timestamp": timestamp,
            "data": data
        }
        file_path = os.path.join(self.storage_path, f"data_{timestamp}.json")
        with open(file_path, 'w') as f:
            json.dump(data_entry, f)
        print(f"Data aggregated and stored at: {file_path}")

    def retrieve_data(self, filename):
        """Retrieves data from a specified JSON file."""
        file_path = os.path.join(self.storage_path, filename)
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                return json.load(f)
        else:
            raise FileNotFoundError(f"No such file: {filename}")

    def list_stored_data(self):
        """Lists all stored data files."""
        return os.listdir(self.storage_path)

# Example usage
if __name__ == "__main__":
    aggregator = DataAggregator()
    sample_data = {"temperature": 22.5, "pressure": 1013}
    aggregator.aggregate_data(sample_data)
    print("Stored files:", aggregator.list_stored_data())
