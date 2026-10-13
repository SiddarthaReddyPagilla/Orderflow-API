
import unittest

from inventory import check_inventory


class TestInventory(unittest.TestCase):

    def test_enough_stock(self):
        result = check_inventory(
            "West Dallas Hub", "WATER-500ML", 5
        )
        self.assertTrue(result)

    def test_insufficient_stock(self):
        result = check_inventory(
            "Coppell Hub", "WATER-500ML", 10
        )
        self.assertFalse(result)

    def test_exact_stock(self):
        result = check_inventory(
            "Coppell Hub", "SNACK-001", 10
        )
        self.assertTrue(result)

    def test_unknown_product(self):
        result = check_inventory(
            "West Dallas Hub", "UNKNOWN-001", 2
        )
        self.assertFalse(result)

    def test_zero_quantity(self):
        result = check_inventory(
            "West Dallas Hub", "WATER-500ML", 0
        )
        self.assertFalse(result)

    def test_unknown_warehouse(self):
        result = check_inventory(
            "Unknown Hub", "WATER-500ML", 2
        )
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
