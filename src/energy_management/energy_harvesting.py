import numpy as np

class EnergyHarvester:
    def __init__(self, efficiency=0.2):
        self.efficiency = efficiency  # Efficiency of the energy harvesting system

    def harvest_energy(self, available_energy):
        """Harvests energy based on available energy and system efficiency."""
        harvested_energy = available_energy * self.efficiency
        return harvested_energy

    def store_energy(self, harvested_energy, storage_capacity, current_storage):
        """Stores harvested energy in a storage system."""
        new_storage = current_storage + harvested_energy
        if new_storage > storage_capacity:
            new_storage = storage_capacity  # Cap at storage capacity
        return new_storage

    def energy_balance(self, current_storage, energy_consumed):
        """Calculates the remaining energy after consumption."""
        remaining_energy = current_storage - energy_consumed
        return max(remaining_energy, 0)  # Ensure non-negative energy

# Example usage
if __name__ == "__main__":
    harvester = EnergyHarvester(efficiency=0.25)  # 25% efficiency
    available_energy = 1000  # Available energy in Watts
    harvested_energy = harvester.harvest_energy(available_energy)
    print(f"Harvested energy: {harvested_energy:.2f} Watts")

    storage_capacity = 5000  # Storage capacity in Watts
    current_storage = 2000  # Current stored energy in Watts
    new_storage = harvester.store_energy(harvested_energy, storage_capacity, current_storage)
    print(f"New energy storage: {new_storage:.2f} Watts")

    energy_consumed = 1500  # Energy consumed in Watts
    remaining_energy = harvester.energy_balance(new_storage, energy_consumed)
    print(f"Remaining energy after consumption: {remaining_energy:.2f} Watts")
