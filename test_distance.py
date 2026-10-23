import unittest
from distance import haversine_distance

class TestDistance(unittest.TestCase):
    def test_same_location(self):
        self.assertEqual(
            haversine_distance(0, 0, 0, 0), 0
        )


class TestDistanceAdditional(unittest.TestCase):

    # Test 2: Known distance at the equator
    def test_known_distance(self):
        result = haversine_distance(0, 0, 0, 1)

        self.assertAlmostEqual(
            result, 111.195, delta=0.02
        )

    # Test 3: Distance from A to B equals B to A
    def test_distance_symmetry(self):
        distance_ab = haversine_distance(
            32.7558565, -96.9041442,
            32.95805, -97.01704
        )

        distance_ba = haversine_distance(
            32.95805, -97.01704,
            32.7558565, -96.9041442
        )

        self.assertAlmostEqual(
            distance_ab, distance_ba, places=8
        )

    # Test 4: Greater separation means greater distance
    def test_increasing_distance(self):
        near = haversine_distance(0, 0, 0, 1)
        far = haversine_distance(0, 0, 0, 2)

        self.assertGreater(far, near)

    # Test 5: DFW warehouse reference points
    def test_dfw_distance(self):
        result = haversine_distance(
            32.7558565, -96.9041442,
            32.95805, -97.01704
        )

        self.assertGreater(result, 0)
        self.assertLess(result, 50)

    # Test 6: International date line
    def test_international_date_line(self):
        result = haversine_distance(
            0, 179, 0, -179
        )

        self.assertAlmostEqual(
            result, 222.39, delta=0.1
        )
