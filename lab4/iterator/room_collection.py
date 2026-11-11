class RoomIterator:
    def __init__(self, rooms):
        self.rooms = rooms
        self.position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.position >= len(self.rooms):
            raise StopIteration

        room = self.rooms[self.position]
        self.position += 1
        return room


class HotelRooms:
    def __init__(self):
        self.rooms = []

    def add_room(self, number):
        self.rooms.append(number)

    def __iter__(self):
        return RoomIterator(self.rooms)
