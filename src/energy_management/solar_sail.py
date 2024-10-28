import numpy as np

class SolarSail:
    def __init__(self, sail_area, solar_constant=1361):
        self.sail_area = sail_area  # in square meters
        self.solar_constant = solar_constant  # W/m^2
        self.thrust = 0  # Initial thrust in Newtons

    def calculate_thrust(self, angle_of_incidence):
        """Calculates the thrust generated by the solar sail."""
        # Thrust = Solar constant * Sail area * cos(angle)
        angle_rad = np.radians(angle_of_incidence)
        self.thrust = self.solar_constant * self.sail_area * np.cos(angle_rad)
        return self.thrust

    def adjust_sail_angle(self, current_angle, desired_angle):
        """Adjusts the sail angle towards the desired angle."""
        adjustment = desired_angle - current_angle
        # Limit the adjustment to a maximum of 5 degrees per time step
        adjustment = np.clip(adjustment, -5, 5)
        new_angle = current_angle + adjustment
        return new_angle

    def simulate_movement(self, initial_velocity, time_step, angle_of_incidence):
        """Simulates the movement of the spacecraft over a time step."""
        thrust = self.calculate_thrust(angle_of_incidence)
        acceleration = thrust / 1000  # Assuming mass of 1000 kg for the spacecraft
        new_velocity = initial_velocity + acceleration * time_step
        return new_velocity

# Example usage
if __name__ == "__main__":
    sail = SolarSail(sail_area=50)  # 50 m^2 sail area
    current_angle = 0  # Initial angle
    desired_angle = 30  # Desired angle
    initial_velocity = 0  # Initial velocity in m/s
    time_step = 1  # Time step in seconds

    # Adjust sail angle
    new_angle = sail.adjust_sail_angle(current_angle, desired_angle)
    print(f"Adjusted sail angle: {new_angle} degrees")

    # Simulate movement
    new_velocity = sail.simulate_movement(initial_velocity, time_step, new_angle)
    print(f"New velocity after {time_step} seconds: {new_velocity:.2f} m/s")
