
from .rooms import StandardRoom, LuxuryRoom


class RoomCreator:
    def create_room(self):
        raise NotImplementedError


class StandardRoomCreator(RoomCreator):
    def create_room(self):
        return StandardRoom()


class LuxuryRoomCreator(RoomCreator):
    def create_room(self):
        return LuxuryRoom()
