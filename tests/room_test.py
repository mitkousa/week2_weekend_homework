import unittest
from src.guest import Guest
from src.room import Room
from src.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):

        self.room1 = Room("Hip-Hop", "10")
        self.room2 = Room("Rock", "15")
        self.room3 = Room("Pop", "20")

        self.song1 = Song("In da club", "50 Cent")
        self.song2 = Song("Ms Jackson", "OutKast")
        self.song3 = Song("Smoke on the water", "Deep purple")
        self.song4 = Song("Smells like teen spirit", "Nirvana")
        self.song5 = Song("Rolling in the deep", "Adele")
        self.song6 = Song("Shape of you", "Ed Sheeran")

        self.guest1 = Guest("Boris Johnson", 57, "British")
        self.guest2 = Guest("Queen Elizabeth", 95, "British")
        self.guest3 = Guest("President Obama", 59, "American")
        self.guest4 = Guest("Will Smith", 52, "American")
        self.guest5 = Guest("Hristo Stoichkov", 56, "Bulgarian")
        self.guest6 = Guest("Dimitar Berbatov", 40, "Bulgarian")

    def test_room_has_genre(self):
        self.assertEqual("Rock", self.room2.genre)

    def test_room_guest_unique_origin(self):
        self.room1.check_in_guest(self.guest5)
        self.assertEqual(["Bulgarian"], self.room1.get_unique_origin(self.guest5))

    def test_room_can_check_in_guest(self):
        self.room1.check_in_guest(self.guest1)
        self.assertEqual(1, self.room1.count_guests())

    def test_room_can_check_out_guest(self):
        self.room2.check_in_guest(self.guest3)
        self.room2.check_in_guest(self.guest6)
        self.room2.check_out_guest(self.guest3)
        self.assertEqual(1, self.room2.count_guests())

    def test_add_song_to_list(self):
        self.room1.add_song_to_list(self.song1)
        self.room1.add_song_to_list(self.song2)
        self.assertEqual(2, self.room1.count_songs())