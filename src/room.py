class Room:

    def __init__(self, genre, capacity):
        self.capacity = capacity
        self.genre = genre
        self.guest_list = []
        self.guest_origin = []

    def count_guests(self):
        return len(self.guest_list)

    def check_in_guest(self, guest):
        self.guest_list.append(guest)

    def check_out_guest(self, guest):
        self.guest_list.remove(guest)

    def get_unique_origin(self, guest):
        self.guest_origin.append(guest.origin)

        return self.guest_origin

    