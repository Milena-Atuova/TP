
from .products import (
    EconomyRoom,
    PremiumRoom,
    EconomyService,
    PremiumService
)


class HotelFactory:
    def create_room(self):
        raise NotImplementedError

    def create_service(self):
        raise NotImplementedError


class EconomyFactory(HotelFactory):
    def create_room(self):
        return EconomyRoom()

    def create_service(self):
        return EconomyService()


class PremiumFactory(HotelFactory):
    def create_room(self):
        return PremiumRoom()

    def create_service(self):
        return PremiumService()
