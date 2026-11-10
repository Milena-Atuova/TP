
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
