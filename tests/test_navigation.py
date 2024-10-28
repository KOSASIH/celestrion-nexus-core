import unittest
from energy_management.solar_sail import SolarSail

class TestSolarSail(unittest.TestCase):
    def setUp(self):
        self.sail = SolarSail(sail_area=50)

    def test_calculate_thrust(self):
        thrust = self.sail.calculate_thrust(angle_of_incidence=0)
        self.assertGreater(thrust, 0)

    def test_adjust_sail_angle(self):
        new_angle = self.sail.adjust_sail_angle(current_angle=0, desired_angle=30)
        self.assertEqual(new_angle, 5)  # Should adjust by max 5 degrees

if __name__ == "__main__":
    unittest.main()
