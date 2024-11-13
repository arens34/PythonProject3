# test_presentation.py

import unittest
from presentation import Presentation
from business import Business
from record import Record

class TestPresentation(unittest.TestCase):

    def setUp(self):
        """Create a Presentation instance for testing."""
        self.presentation = Presentation()
        self.presentation.business = Business()  # Ensure business is initialized

    def test_add_record(self):
        """Test that a new record can be added through the presentation layer."""
        record_data = {
            'date': '2024-10-13',
            'month': 'October',
            'year': '2024',
            'company': 'Example Company',
            'pipeline': 'Example Pipeline',
            'key_point': 'Example Key Point',
            'latitude': 12.34,
            'longitude': 56.78,
            'direction_of_flow': 'North',
            'trade_type': 'Import',
            'product': 'Oil',
            'throughput': 100.0,
            'committed_volumes': 80.0,
            'uncommitted_volumes': 20.0,
            'nameplate_capacity': 120.0,
            'available_capacity': 100.0,
            'reason_for_variance': 'N/A'
        }
        
        expected_record = Record(**record_data)
        self.presentation.business.add_record(expected_record)

        self.assertEqual(len(self.presentation.business.records), 1)

        actual_record = self.presentation.business.records[0]
        self.assertEqual(actual_record.date, expected_record.date)
        self.assertEqual(actual_record.month, expected_record.month)
        self.assertEqual(actual_record.year, expected_record.year)
        self.assertEqual(actual_record.company, expected_record.company)
        self.assertEqual(actual_record.pipeline, expected_record.pipeline)
        self.assertEqual(actual_record.key_point, expected_record.key_point)
        self.assertEqual(actual_record.latitude, expected_record.latitude)
        self.assertEqual(actual_record.longitude, expected_record.longitude)
        self.assertEqual(actual_record.direction_of_flow, expected_record.direction_of_flow)
        self.assertEqual(actual_record.trade_type, expected_record.trade_type)
        self.assertEqual(actual_record.product, expected_record.product)
        self.assertEqual(actual_record.throughput, expected_record.throughput)
        self.assertEqual(actual_record.committed_volumes, expected_record.committed_volumes)
        self.assertEqual(actual_record.uncommitted_volumes, expected_record.uncommitted_volumes)
        self.assertEqual(actual_record.nameplate_capacity, expected_record.nameplate_capacity)
        self.assertEqual(actual_record.available_capacity, expected_record.available_capacity)
        self.assertEqual(actual_record.reason_for_variance, expected_record.reason_for_variance)

    def tearDown(self):
        """Print the name of the user after tests."""
        print("Tests completed by: Aaron Renshaw")

if __name__ == '__main__':
    unittest.main()
