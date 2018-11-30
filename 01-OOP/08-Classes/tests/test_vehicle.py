import unittest
from vehicle import Vehicle

class VehicleTest(unittest.TestCase):
    def test_initialization(self):
        car = Vehicle("Ferrari", "red")
        self.assertEqual(car.brand, "Ferrari")
        self.assertEqual(car.color, "red")

    def test_car_is_stopped_at_initialization(self):
        car = Vehicle("Lotus", "Black")
        self.assertFalse(car.started)

    def test_car_can_be_started(self):
        car = Vehicle("Lotus", "Black")
        car.start() # Calling an instance method that you need to implement
        self.assertTrue(car.started)

    def test_car_can_be_stopped(self):
        car = Vehicle("Lotus", "Black")
        car.start()
        car.stop()
        self.assertFalse(car.started)
