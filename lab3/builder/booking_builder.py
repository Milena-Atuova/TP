
from .booking import Booking


class BookingBuilder:
    def __init__(self):
        self.guest = None
        self.room = None
        self.nights = None
        self.breakfast = False
        self.transfer = False

    def set_guest(self, guest):
        self.guest = guest
        return self

    def set_room(self, room):
        self.room = room
        return self

    def set_nights(self, nights):
        self.nights = nights
        return self

    def add_breakfast(self):
        self.breakfast = True
        return self

    def add_transfer(self):
        self.transfer = True
        return self

    def build(self):
        if self.guest is None or self.room is None or self.nights is None:
            raise ValueError("Не все обязательные данные заполнены")

        if not isinstance(self.nights, int) or isinstance(self.nights, bool) or self.nights <= 0:
            raise ValueError("Количество ночей должно быть положительным целым числом")

        return Booking(
            self.guest,
            self.room,
            self.nights,
            self.breakfast,
            self.transfer
        )
