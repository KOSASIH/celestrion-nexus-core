import numpy as np
import random
import json
from datetime import datetime

class QuantumComm:
    def __init__(self):
        self.entangled_pairs = []  # List to store entangled pairs
        self.max_pairs = 10        # Maximum number of entangled pairs

    def create_entangled_pair(self):
        """Simulates the creation of an entangled quantum pair."""
        if len(self.entangled_pairs) < self.max_pairs:
            # Generate a random 2x2 matrix representing quantum states
            pair = np.random.rand(2, 2)  # Placeholder for actual quantum states
            self.entangled_pairs.append(pair)
            print(f"Entangled pair created: {pair}")
            return pair
        else:
            raise Exception("Maximum number of entangled pairs reached.")

    def measure_state(self, pair_index):
        """Measures the state of a quantum pair."""
        if pair_index < len(self.entangled_pairs):
            state = self.entangled_pairs[pair_index]
            # Simulate measurement with a probabilistic outcome
            measurement = np.random.choice([0, 1], p=[0.5, 0.5])
            print(f"Measured state of pair {pair_index}: {measurement}")
            return measurement
        else:
            raise IndexError("Entangled pair index out of range.")

    def transmit_message(self, message, pair_index):
        """Transmits a message using the entangled pair."""
        if pair_index < len(self.entangled_pairs):
            # Simulate message transmission using quantum entanglement
            print(f"Transmitting message: '{message}' using entangled pair {pair_index}.")
            # Simulate a potential error in transmission
            if random.random() < 0.1:  # 10% chance of transmission error
                raise Exception("Transmission error occurred.")
            return True
        else:
            raise IndexError("Entangled pair index out of range.")

    def receive_message(self, pair_index):
        """Simulates receiving a message by measuring the state of the entangled pair."""
        if pair_index < len(self.entangled_pairs):
            measurement = self.measure_state(pair_index)
            # Simulate message reconstruction based on measurement
            reconstructed_message = f"Message received with measurement: {measurement}"
            print(reconstructed_message)
            return reconstructed_message
        else:
            raise IndexError("Entangled pair index out of range.")

    def format_message(self, recipient, message):
        """Formats a message for transmission."""
        formatted_message = {
            "recipient": recipient,
            "message": message,
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }
        return json.dumps(formatted_message)

    def parse_message(self, raw_message):
        """Parses a raw message string into a dictionary."""
        try:
            message_dict = json.loads(raw_message)
            return message_dict
        except json.JSONDecodeError:
            raise ValueError("Invalid message format.")

    def validate_message(self, message_dict):
        """Validates the structure of the message."""
        required_keys = ["recipient", "message", "timestamp"]
        for key in required_keys:
            if key not in message_dict:
                raise ValueError(f"Missing required key: {key}")
        return True

# Example usage
if __name__ == "__main__":
    quantum_comm = QuantumComm()
    
    # Create entangled pairs
    for _ in range(3):
        quantum_comm.create_entangled_pair()
    
    # Format a message
    message = quantum_comm.format_message("recipient@example.com", "Hello, Quantum World!")
    
    # Transmit the message using the first entangled pair
    try:
        quantum_comm.transmit_message(message, 0)
    except Exception as e:
        print(e)

    # Receive a message using the first entangled pair
    try:
        quantum_comm.receive_message(0)
    except Exception as e:
        print(e)
