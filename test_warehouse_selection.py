
import unittest

from warehouse_selection import find_eligible_warehouses


class TestWarehouseSelection(unittest.TestCase):

    def test_multiple_eligible_warehouses(self):
        result = find_eligible_warehouses("WATER-500ML", 5)

        self.assertEqual(
            result,
            ["West Dallas Hub", "Coppell Hub"]
        )

    def test_no_warehouse_has_enough_stock(self):
        result = find_eligible_warehouses("WATER-500ML", 25)

        self.assertEqual(result, [])

    def test_only_one_eligible_warehouse(self):
        result = find_eligible_warehouses("SNACK-001", 20)

        self.assertEqual(
            result,
            ["North Fort Worth Hub"]
        )

    def test_unknown_product(self):
        result = find_eligible_warehouses("UNKNOWN-001", 5)

        self.assertEqual(result, [])

    def test_invalid_quantity(self):
        result = find_eligible_warehouses("WATER-500ML", 0)

        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
