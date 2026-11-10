
class Booking:
    def __init__(self, guest, room, nights, breakfast=False, transfer=False):
        self.guest = guest
        self.room = room
        self.nights = nights
        self.breakfast = breakfast
        self.transfer = transfer

    def show_info(self):
        print("Гость:", self.guest)
        print("Номер:", self.room)
        print("Количество ночей:", self.nights)
        print("Завтрак:", "Да" if self.breakfast else "Нет")
        print("Трансфер:", "Да" if self.transfer else "Нет")
