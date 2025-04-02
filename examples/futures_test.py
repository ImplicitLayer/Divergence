from divergence.futures.hedging import *
from divergence.futures.pricing import *
from divergence.futures.strategies import *
import numpy as np

# Параметры активов
spot_price_a = 100
quantity_a = 1000
futures_price_a = 95

spot_price_b = 90
quantity_b = 500
futures_price_b = 85

# Комиссия
commission_rate = 0.01

# Примеры хеджирования
print("Прямое хеджирование:", direct_hedging(spot_price_a, futures_price_a, quantity_a, commission_rate))
print("Косвенное хеджирование:",
      indirect_hedging(spot_price_a, futures_price_a, quantity_a, spot_price_b, futures_price_b, quantity_b,
                       commission_rate))
print("Полное хеджирование:", full_hedging(spot_price_a, futures_price_a, quantity_a, commission_rate))
print("Частичное хеджирование (50%):",
      partial_hedging(spot_price_a, futures_price_a, quantity_a, hedge_ratio=0.5, commission_rate=commission_rate))
print("Долгосрочное хеджирование (12 месяцев):",
      long_term_hedging(spot_price_a, futures_price_a, quantity_a, time_period=12, commission_rate=commission_rate))
print("Краткосрочное хеджирование (1 месяц):",
      short_term_hedging(spot_price_a, futures_price_a, quantity_a, time_period=1, commission_rate=commission_rate))
print("Хеджирование с использованием опционов:", options_hedging(spot_price_a, 90, quantity_a, commission_rate))
# print("Кросс-хеджирование:",
#       cross_hedging(spot_price_a, futures_price_a, quantity_a, spot_price_b, futures_price_b, quantity_b,
#                     commission_rate))


# Пример использования моделей
spot_price = 75  # Текущая цена актива
risk_free_rate = 0.01  # Безрисковая ставка
time_to_expiration = 1  # Время до истечения контракта (в годах)
storage_cost = 2  # Стоимость хранения
dividends = 1  # Дивиденды
demand_factor = 0.1  # Фактор спроса
supply_factor = 0.05  # Фактор предложения
volatility = 0.2  # Волатильность актива

# Расчет цен по различным моделям
kaplan_sharpe_price = calculate_kaplan_sharpe_price(spot_price, 0, risk_free_rate, time_to_expiration)
cost_of_carry_price = calculate_cost_of_carry_price(spot_price, storage_cost, risk_free_rate, time_to_expiration,
                                                    dividends)
hanna_price = calculate_hanna_price(spot_price, demand_factor, supply_factor)
gaussian_price = calculate_gaussian_price(spot_price, volatility, time_to_expiration)

print(f"Цена по модели Каплана-Шарпа: {kaplan_sharpe_price:.2f}")
print(f"Цена по модели стоимости хранения: {cost_of_carry_price:.2f}")
print(f"Цена по модели Ханна: {hanna_price:.2f}")
print(f"Цена по модели Гаусса: {gaussian_price:.2f}")

prices = np.array([100, 105, 110, 120])  # Пример цен
initial_investment = 1000
final_value = buy_and_hold(prices, initial_investment)
print(f"Покупка и удержание: Конечная стоимость = {final_value}")

# 2. Арбитраж
price_a = 50
price_b = 55
quantity = 10
arbitrage_profit = arbitrage(price_a, price_b, quantity)
print(f"Арбитраж: Потенциальная прибыль = {arbitrage_profit}")

# 3. Короткая продажа
initial_price = 100
final_price = 90
short_quantity = 5
short_profit = short_selling(initial_price, final_price, short_quantity)
print(f"Короткая продажа: Потенциальная прибыль/убыток = {short_profit}")

# 4. Кросс-хеджирование
futures_price = 200
spot_price = 190
hedge_ratio = 1.5
hedge_quantity = 10
hedged_value = cross_hedging(futures_price, spot_price, hedge_ratio, hedge_quantity)
print(f"Кросс-хеджирование: Защищенная стоимость = {hedged_value}")

# 5. Торговля на основе волатильности
volatility_index = 25
position_size = 100
threshold = 20
volatility_profit = volatility_trading(volatility_index, position_size, threshold)
print(f"Торговля на основе волатильности: Потенциальная прибыль = {volatility_profit}")

# 6. Параллельная торговля
price_a = 120
price_b = 115
pairs_quantity = 10
pairs_threshold = 5
pairs_profit = pairs_trading(price_a, price_b, pairs_quantity, pairs_threshold)
print(f"Параллельная торговля: Потенциальная прибыль = {pairs_profit}")
