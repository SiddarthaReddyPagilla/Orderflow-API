
# DispatchForge - Warehouse Ranking Tests

import unittest
from copy import deepcopy

from inventory import inventory
from warehouse_ranking import rank_warehouses


class TestWarehouseRanking(unittest.TestCase):

    def setUp(self):
        # Save our simulated inventory before each test.
        self.original_inventory = deepcopy(inventory)

    def tearDown(self):
        # Restore the inventory after each test.
        inventory.clear()
        inventory.update(self.original_inventory)

    # Test 1: Warehouse with the most stock comes first
    def test_highest_stock_first(self):
        result = rank_warehouses("WATER-500ML", 5)

        self.assertEqual(
            result,
            ["West Dallas Hub", "Coppell Hub"]
        )

    # Test 2: Ranking changes when stock changes
    def test_ranking_changes_with_stock(self):
        inventory["West Dallas Hub"]["WATER-500ML"] = 6
        inventory["Coppell Hub"]["WATER-500ML"] = 12

        result = rank_warehouses("WATER-500ML", 5)

        self.assertEqual(
            result,
            ["Coppell Hub", "West Dallas Hub"]
        )

    # Test 3: Only one warehouse can fulfill an order
    def test_single_eligible_warehouse(self):
        result = rank_warehouses("SNACK-001", 20)

        self.assertEqual(
            result,
            ["North Fort Worth Hub"]
        )

    # Test 4: No warehouse has enough inventory
    def test_insufficient_stock(self):
        result = rank_warehouses("WATER-500ML", 25)

        self.assertEqual(result, [])

    # Test 5: Product does not exist
    def test_unknown_product(self):
        result = rank_warehouses("UNKNOWN-001", 5)

        self.assertEqual(result, [])

    # Test 6: Invalid requested quantity
    def test_invalid_quantity(self):
        self.assertEqual(
            rank_warehouses("WATER-500ML", 0),
            []
        )

        self.assertEqual(
            rank_warehouses("WATER-500ML", -1),
            []
        )

    # Test 7: Warehouses have equal stock
    def test_equal_stock(self):
        inventory["West Dallas Hub"]["WATER-500ML"] = 20
        inventory["Coppell Hub"]["WATER-500ML"] = 20

        result = rank_warehouses("WATER-500ML", 5)

        self.assertEqual(len(result), 2)
        self.assertEqual(
            set(result),
            {"West Dallas Hub", "Coppell Hub"}
        )

    # Test 8: Ranking must not change inventory
    def test_ranking_does_not_change_inventory(self):
        before = deepcopy(inventory)

        rank_warehouses("WATER-500ML", 5)

        self.assertEqual(inventory, before)


if __name__ == "__main__":
    unittest.main()
