
from singleton.hotel_settings import HotelSettings

settings1 = HotelSettings()
settings2 = HotelSettings()

settings1.show_info()

print("Это один объект?", settings1 is settings2)

