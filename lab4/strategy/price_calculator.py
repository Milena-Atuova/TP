class PriceCalculator:
    def __init__(self, tariff):
        self.tariff = tariff

    def set_tariff(self, tariff):
        self.tariff = tariff

    def calculate_price(self, price, nights):
        return self.tariff.calculate(price, nights)