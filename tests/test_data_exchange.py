import unittest
from data_exchange.data_aggregator import DataAggregator

class TestDataAggregator(unittest.TestCase):
    def setUp(self):
        self.aggregator = DataAggregator()

    def test_aggregate_data(self):
        sample_data = {"energy_harvested": 100, "energy_storage": 200}
        self.aggregator.aggregate_data(sample_data)
        self.assertIn("data_0.json", self.aggregator.list_stored_data())

    def test_list_stored_data(self):
        self.aggregator.aggregate_data({"energy_harvested": 100})
        files = self.aggregator.list_stored_data()
        self.assertGreater(len(files), 0)

if __name__ == "__main__":
    unittest.main()
