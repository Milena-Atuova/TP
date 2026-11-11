from strategy.tariffs import RegularTariff, LoyalGuestTariff, WeekendTariff
from strategy.price_calculator import PriceCalculator

print("Strategy — расчет стоимости проживания")

calculator = PriceCalculator(RegularTariff())

print("Обычный тариф:", calculator.calculate_price(3000, 3))

calculator.set_tariff(LoyalGuestTariff())
print("Постоянный гость:", calculator.calculate_price(3000, 3))

calculator.set_tariff(WeekendTariff())
print("Тариф выходного дня:", calculator.calculate_price(3000, 3))




from chain.booking_checks import GuestCheck, NightsCheck, RoomsCheck

print("\nChain of Responsibility — проверка бронирования")

guest_check = GuestCheck()
nights_check = NightsCheck()
rooms_check = RoomsCheck()

guest_check.set_next(nights_check).set_next(rooms_check)

booking = {
    "guest": "Милена",
    "nights": 3,
    "available_rooms": 5
}

print(guest_check.check(booking))

booking["available_rooms"] = 0
print(guest_check.check(booking))




from iterator.room_collection import HotelRooms

print("\nIterator — номера отеля")

hotel = HotelRooms()

hotel.add_room(101)
hotel.add_room(102)
hotel.add_room(201)
hotel.add_room(202)

for room in hotel:
    print("Номер:", room)
