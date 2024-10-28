import json
import requests

class DataSharingProtocol:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def send_data(self, data):
        """Sends data to a specified endpoint using HTTP POST."""
        headers = {'Content-Type': 'application/json'}
        response = requests.post(self.endpoint, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            print("Data sent successfully.")
        else:
            print(f"Failed to send data. Status code: {response.status_code}, Response: {response.text}")

    def receive_data(self):
        """Receives data from the specified endpoint using HTTP GET."""
        response = requests.get(self.endpoint)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to receive data. Status code: {response.status_code}, Response: {response.text}")
            return None

# Example usage
if __name__ == "__main__":
    sharing_protocol = DataSharingProtocol(endpoint="http://example.com/api/data")
    sample_data = {"temperature": 22.5, "pressure": 1013}
    sharing_protocol.send_data(sample_data)
    received_data = sharing_protocol.receive_data()
    print("Received data:", received_data)
