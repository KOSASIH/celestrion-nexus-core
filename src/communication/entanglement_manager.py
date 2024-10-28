import random
from quantum_comm import QuantumComm

class EntanglementManager:
    def __init__(self):
        self.quantum_comm = QuantumComm()
        self.active_pairs = []  # List to keep track of active entangled pairs

    def establish_connection(self):
        """Establishes a quantum connection by creating entangled pairs."""
        print("Establishing quantum connection...")
        try:
            pair = self.quantum_comm.create_entangled_pair()
            self.active_pairs.append(pair)
            print(f"Entangled pair established: {pair}")
            return len(self.active_pairs) - 1  # Return the index of the new pair
        except Exception as e:
            print(f"Failed to establish connection: {e}")
            return None

    def send_message(self, message, pair_index):
        """Sends a message using the established quantum connection."""
        if pair_index < len(self.active_pairs):
            try:
                print(f"Sending message through entangled pair {pair_index}...")
                success = self.quantum_comm.transmit_message(message, pair_index)
                if success:
                    print("Message sent successfully.")
            except Exception as e:
                print(f"Error sending message: {e}")
        else:
            print("Invalid pair index. Cannot send message.")

    def receive_message(self, pair_index):
        """Simulates receiving a message by measuring the state of the entangled pair."""
        if pair_index < len(self.active_pairs):
            try:
                print(f"Receiving message through entangled pair {pair_index}...")
                measurement = self.quantum_comm.receive_message(pair_index)
                print(f"Received measurement: {measurement}")
                return measurement
            except Exception as e:
                print(f"Error receiving message: {e}")
        else:
            print("Invalid pair index. Cannot receive message.")

    def list_active_pairs(self):
        """Lists all active entangled pairs."""
        print(f"Active entangled pairs: {len(self.active_pairs)}")
        for index, pair in enumerate(self.active_pairs):
            print(f"Pair {index}: {pair}")

    def remove_pair(self, pair_index):
        """Removes an entangled pair from the active list."""
        if pair_index < len(self.active_pairs):
            removed_pair = self.active_pairs.pop(pair_index)
            print(f"Removed entangled pair: {removed_pair}")
        else:
            print("Invalid pair index. Cannot remove pair.")

# Example usage
if __name__ == "__main__":
    entanglement_manager = EntanglementManager()
    
    # Establish connections
    for _ in range(3):
        entanglement_manager.establish_connection()
    
    # List active pairs
    entanglement_manager.list_active_pairs()
    
    # Format a message
    message = entanglement_manager.quantum_comm.format_message("recipient@example.com", "Hello, Quantum World!")
    
    # Send the message using the first entangled pair
    entanglement_manager.send_message(message, 0)
    
    # Receive a message using the first entangled pair
    entanglement_manager.receive_message(0)
    
    # Remove an entangled pair
    entanglement_manager.remove_pair(1)
    
    # List active pairs again
    entanglement_manager.list_active_pairs()
