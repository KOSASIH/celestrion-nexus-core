import json
import base64

class UniversalProtocol:
    def __init__(self, version="1.0"):
        self.version = version

    def encode_message(self, message, language="en"):
        """Encodes a message into a universal format."""
        encoded_message = {
            "version": self.version,
            "language": language,
            "content": base64.b64encode(message.encode()).decode()
        }
        return json.dumps(encoded_message)

    def decode_message(self, encoded_message):
        """Decodes a message from the universal format."""
        message_data = json.loads(encoded_message)
        decoded_content = base64.b64decode(message_data["content"]).decode()
        return {
            "version": message_data["version"],
            "language": message_data["language"],
            "content": decoded_content
        }

# Example usage
if __name__ == "__main__":
    protocol = UniversalProtocol()
    message = "Hello, this is a test message."
    
    # Encode the message
    encoded = protocol.encode_message(message, language="en")
    print("Encoded message:", encoded)

    # Decode the message
    decoded = protocol.decode_message(encoded)
    print("Decoded message:", decoded)
