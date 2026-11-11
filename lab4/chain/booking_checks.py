
class BookingCheck:
    def __init__(self):
        self.next_check = None

    def set_next(self, check):
        self.next_check = check
        return check

    def check(self, booking):
        if self.next_check:
            return self.next_check.check(booking)
        return "Бронирование подтверждено"


class GuestCheck(BookingCheck):
    def check(self, booking):
        if not booking["guest"].strip():
            return "Ошибка: не указано имя гостя"
        return super().check(booking)


class NightsCheck(BookingCheck):
    def check(self, booking):
        if booking["nights"] <= 0:
            return "Ошибка: неверное количество ночей"
        return super().check(booking)


class RoomsCheck(BookingCheck):
    def check(self, booking):
        if booking["available_rooms"] <= 0:
            return "Ошибка: нет свободных номеров"
        return super().check(booking)
