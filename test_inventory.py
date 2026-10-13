
import unittest
from copy import deepcopy

from inventory import inventory, check_inventory, reserve_inventory


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

class TestInventoryReservation(unittest.TestCase):

    def setUp(self):
        # Save inventory before each test
        self.original_inventory = deepcopy(inventory)

    def tearDown(self):
        # Restore inventory after each test
        inventory.clear()
        inventory.update(self.original_inventory)

    def test_successful_reservation(self):
        result = reserve_inventory(
            "West Dallas Hub", "WATER-500ML", 5
        )

        self.assertTrue(result)
        self.assertEqual(
            inventory["West Dallas Hub"]["WATER-500ML"], 15
        )

    def test_insufficient_stock_reservation(self):
        result = reserve_inventory(
            "Coppell Hub", "WATER-500ML", 10
        )

        self.assertFalse(result)
        self.assertEqual(
            inventory["Coppell Hub"]["WATER-500ML"], 7
        )

    def test_exact_stock_reservation(self):
        result = reserve_inventory(
            "Coppell Hub", "SNACK-001", 10
        )

        self.assertTrue(result)
        self.assertEqual(
            inventory["Coppell Hub"]["SNACK-001"], 0
        )

    def test_prevent_multiple_reservations(self):
        first_order = reserve_inventory(
            "Coppell Hub", "WATER-500ML", 5
        )

        second_order = reserve_inventory(
            "Coppell Hub", "WATER-500ML", 3
        )

        self.assertTrue(first_order)
        self.assertFalse(second_order)
        self.assertEqual(
            inventory["Coppell Hub"]["WATER-500ML"], 2
        )
