
from singleton.hotel_settings import HotelSettings

settings1 = HotelSettings()
settings2 = HotelSettings()

settings1.show_info()

print("Это один объект?", settings1 is settings2)


from factory_method.creators import StandardRoomCreator, LuxuryRoomCreator

print("\nFactory Method:")

standard = StandardRoomCreator().create_room()
luxury = LuxuryRoomCreator().create_room()

print(standard.get_info())
print(luxury.get_info())



from abstract_factory.factories import EconomyFactory, PremiumFactory

print("\nAbstract Factory:")

economy = EconomyFactory()
premium = PremiumFactory()

print("Эконом:")
print(economy.create_room().get_info())
print(economy.create_service().get_info())

print("Премиум:")
print(premium.create_room().get_info())
print(premium.create_service().get_info())


from builder.booking_builder import BookingBuilder

print("\nBuilder:")

booking = (
    BookingBuilder()
    .set_guest("Милена")
    .set_room("Люкс")
    .set_nights(3)
    .add_breakfast()
    .add_transfer()
    .build()
)

booking.show_info()
