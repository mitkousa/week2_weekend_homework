import unittest
from src.guest import Guest
from src.room import Room
from src.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):

        self.room1 = Room("Hip-Hop")
        self.room2 = Room("Rock")
        self.room3 = Room("Pop")

        self.song1 = Song("In da club", "50 Cent")
        self.song2 = Song("Ms Jackson", "OutKast")
        self.song3 = Song("Smoke on the water", "Deep purple")
        self.song4 = Song("Smells like teen spirit", "Nirvana")
        self.song5 = Song("Rolling in the deep", "Adele")
        self.song6 = Song("Shape of you", "Ed Sheeran")

        self.guest1 = Guest("Boris Johnson")
        self.guest2 = Guest("Queen Elizabeth")
        self.guest3 = Guest("President Obama")

        def test_room_has_genre(self):
            self.assertEqual("Rock", self.room.genre)