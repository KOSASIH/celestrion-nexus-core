import json
from datetime import datetime

class MessageProtocol:
    @staticmethod
    def format_message(recipient, message, metadata=None):
        """Formats a message for transmission with optional metadata."""
        formatted_message = {
            "recipient": recipient,
            "message": message,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "metadata": metadata or {}
        }
        return json.dumps(formatted_message)

    @staticmethod
    def parse_message(raw_message):
        """Parses a raw message string into a dictionary."""
        try:
            message_dict = json.loads(raw_message)
            return message_dict
        except json.JSONDecodeError:
            raise ValueError("Invalid message format.")

    @staticmethod
    def validate_message(message_dict):
        """Validates the structure of the message."""
        required_keys = ["recipient", "message", "timestamp"]
        for key in required_keys:
            if key not in message_dict:
                raise ValueError(f"Missing required key: {key}")
        
        # Additional validation for metadata if present
        if "metadata" in message_dict and not isinstance(message_dict["metadata"], dict):
            raise ValueError("Metadata must be a dictionary.")
        
        return True

    @staticmethod
    def add_metadata(message_dict, key, value):
        """Adds metadata to an existing message dictionary."""
        if "metadata" not in message_dict:
            message_dict["metadata"] = {}
        message_dict["metadata"][key] = value

    @staticmethod
    def remove_metadata(message_dict, key):
        """Removes a key from the metadata of a message dictionary."""
        if "metadata" in message_dict and key in message_dict["metadata"]:
            del message_dict["metadata"][key]

    @staticmethod
    def get_metadata(message_dict, key):
        """Retrieves a value from the metadata of a message dictionary."""
        return message_dict.get("metadata", {}).get(key, None)

# Example usage
if __name__ == "__main__":
    # Create a message
    message = MessageProtocol.format_message("recipient@example.com", "Hello, Quantum World!", {"priority": "high"})
    
    # Parse the message
    parsed_message = MessageProtocol.parse_message(message)
    print("Parsed Message:", parsed_message)
    
    # Validate the message
    try:
        MessageProtocol.validate_message(parsed_message)
        print("Message is valid.")
    except ValueError as e:
        print(f"Validation error: {e}")
    
    # Add metadata
    MessageProtocol.add_metadata(parsed_message, "session_id", "12345")
    print("Updated Message with Metadata:", parsed_message)
    
    # Retrieve metadata
    session_id = MessageProtocol.get_metadata(parsed_message, "session_id")
    print("Session ID:", session_id)
    
    # Remove metadata
    MessageProtocol.remove_metadata(parsed_message, "priority")
    print("Message after removing priority metadata:", parsed_message)
