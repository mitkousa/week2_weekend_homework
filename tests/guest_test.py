import unittest
from src.guest import Guest
from src.room import Room
from src.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Boris Johnson", 57, "British")
        self.guest2 = Guest("Queen Elizabeth", 95, "British")
        self.guest3 = Guest("President Obama", 59, "American")
        self.guest4 = Guest("Will Smith", 52, "American")
        self.guest5 = Guest("Hristo Stoichkov", 56, "Bulgarian")
        self.guest6 = Guest("Dimitar Berbatov", 40, "Bulgarian")

    def test_guest_has_name(self):
        self.assertEqual("Boris Johnson", self.guest1.name)

    def test_guest_has_age(self):
        self.assertEqual(56, self.guest5.age)

    def test_guest_has_origin(self):
        self.assertEqual("American", self.guest4.origin)