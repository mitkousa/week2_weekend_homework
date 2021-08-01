import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song1 = Song("In da club", "50 Cent")
        self.song2 = Song("Ms Jackson", "OutKast")
        self.song3 = Song("Smoke on the water", "Deep purple")
        self.song4 = Song("Smells like teen spirit", "Nirvana")
        self.song5 = Song("Rolling in the deep", "Adele")
        self.song6 = Song("Shape of you", "Ed Sheeran")

    def test_song_has_title(self):
        self.assertEqual("In da club", self.song1.title)

    def test_song_has_singer(self):
        self.assertEqual("Adele", self.song5.singer)
