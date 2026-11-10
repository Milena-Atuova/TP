
class Room:
    def get_info(self):
        raise NotImplementedError


class Service:
    def get_info(self):
        raise NotImplementedError


class EconomyRoom(Room):
    def get_info(self):
        return "Стандартный номер"


class PremiumRoom(Room):
    def get_info(self):
        return "Номер люкс"


class EconomyService(Service):
    def get_info(self):
        return "Обычное обслуживание"


class PremiumService(Service):
    def get_info(self):
        return "VIP-обслуживание"
