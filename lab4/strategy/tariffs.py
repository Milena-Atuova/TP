
class Tariff:
    def calculate(self, price, nights):
        raise NotImplementedError


class RegularTariff(Tariff):
    def calculate(self, price, nights):
        return price * nights


class LoyalGuestTariff(Tariff):
    def calculate(self, price, nights):
        return price * nights * 0.9


class WeekendTariff(Tariff):
    def calculate(self, price, nights):
        return price * nights * 1.2
