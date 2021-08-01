class Room:

    def __init__(self, genre, capacity):
        self.capacity = capacity
        self.genre = genre
        self.guest_list = []
        self.guest_origin = []
        self.songs_list = []

    def count_guests(self):
        return len(self.guest_list)

    def count_songs(self):
        return len(self.songs_list)

    def check_in_guest(self, guest):
        self.guest_list.append(guest)

    def check_out_guest(self, guest):
        self.guest_list.remove(guest)

    def get_unique_origin(self, guest):
        self.guest_origin.append(guest.origin)
        return self.guest_origin

    def add_song_to_list(self, song):
        self.songs_list.append(song.title)
        return len(self.songs_list)

    