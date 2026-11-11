from strategy.tariffs import RegularTariff, LoyalGuestTariff, WeekendTariff
from strategy.price_calculator import PriceCalculator

print("Strategy — расчет стоимости проживания")

calculator = PriceCalculator(RegularTariff())

print("Обычный тариф:", calculator.calculate_price(3000, 3))

calculator.set_tariff(LoyalGuestTariff())
print("Постоянный гость:", calculator.calculate_price(3000, 3))

calculator.set_tariff(WeekendTariff())
print("Тариф выходного дня:", calculator.calculate_price(3000, 3))