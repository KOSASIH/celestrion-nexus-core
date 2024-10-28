import json
from energy_management.solar_sail import SolarSail
from energy_management.energy_harvesting import EnergyHarvester
from communication_protocols.universal_protocol import UniversalProtocol
from communication_protocols.nlp_engine import NLPEngine
from data_exchange.data_aggregator import DataAggregator
from data_exchange.data_sharing_protocol import DataSharingProtocol
from data_exchange.analytics import DataAnalytics

def main():
    # Initialize components
    print("Initializing components...")
    
    # Energy Management
    solar_sail = SolarSail(sail_area=50)  # 50 m^2 sail area
    energy_harvester = EnergyHarvester(efficiency=0.25)  # 25% efficiency
    data_aggregator = DataAggregator()
    
    # Communication Protocols
    universal_protocol = UniversalProtocol()
    nlp_engine = NLPEngine()
    
    # Simulate energy harvesting
    available_energy = 1000  # Available energy in Watts
    harvested_energy = energy_harvester.harvest_energy(available_energy)
    print(f"Harvested energy: {harvested_energy:.2f} Watts")
    
    # Store harvested energy
    storage_capacity = 5000  # Storage capacity in Watts
    current_storage = 2000  # Current stored energy in Watts
    new_storage = energy_harvester.store_energy(harvested_energy, storage_capacity, current_storage)
    print(f"New energy storage: {new_storage:.2f} Watts")
    
    # Simulate solar sail thrust
    angle_of_incidence = 30  # Angle in degrees
    thrust = solar_sail.calculate_thrust(angle_of_incidence)
    print(f"Calculated thrust: {thrust:.2f} Newtons")
    
    # Encode and decode a message
    message = "Hello, this is a test message."
    encoded_message = universal_protocol.encode_message(message, language="en")
    print("Encoded message:", encoded_message)
    
    decoded_message = universal_protocol.decode_message(encoded_message)
    print("Decoded message:", decoded_message)
    
    # Analyze text using NLP
    text = "Hello, I would like to know more about your services."
    analysis = nlp_engine.analyze_text(text)
    print("Text Analysis:", analysis)
    
    # Generate a response
    response = nlp_engine.generate_response(text)
    print("Generated Response:", response)
    
    # Aggregate and store data
    sample_data = {"energy_harvested": harvested_energy, "energy_storage": new_storage}
    data_aggregator.aggregate_data(sample_data)
    print("Data aggregated and stored.")
    
    # List stored data files
    stored_files = data_aggregator.list_stored_data()
    print("Stored data files:", stored_files)

if __name__ == "__main__":
    main()
