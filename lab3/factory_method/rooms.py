
class Room:
    def get_info(self):
        raise NotImplementedError


class StandardRoom(Room):
    def get_info(self):
        return "Стандартный номер - 3000 руб/ночь"


class LuxuryRoom(Room):
    def get_info(self):
        return "Люкс - 8000 руб/ночь"
