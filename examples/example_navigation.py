from energy_management.solar_sail import SolarSail
from energy_management.energy_harvesting import EnergyHarvester

def main():
    # Initialize the solar sail and energy harvester
    sail_area = 50  # in square meters
    solar_sail = SolarSail(sail_area=sail_area)
    energy_harvester = EnergyHarvester(efficiency=0.25)  # 25% efficiency

    # Simulate energy harvesting
    available_energy = 1000  # Watts
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
    print(f"Calculated thrust at {angle_of_incidence} degrees: {thrust:.2f} Newtons")

    # Adjust sail angle
    current_angle = 0
    desired_angle = 30
    adjusted_angle = solar_sail.adjust_sail_angle(current_angle, desired_angle)
    print(f"Adjusted sail angle from {current_angle} to {adjusted_angle} degrees.")

if __name__ == "__main__":
    main()
