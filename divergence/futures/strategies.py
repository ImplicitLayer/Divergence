import numpy as np


def buy_and_hold(prices, initial_investment):
    shares = initial_investment / prices[0]  # Количество акций, которые можно купить
    final_value = shares * prices[-1]  # Конечная стоимость
    return final_value


def arbitrage(price_a, price_b, quantity):
    if price_a < price_b:
        profit = (price_b - price_a) * quantity
        return profit
    else:
        return 0  # Нет возможности для арбитража


def short_selling(initial_price, final_price, quantity):
    if final_price < initial_price:
        profit = (initial_price - final_price) * quantity
        return profit
    else:
        loss = (final_price - initial_price) * quantity
        return -loss  # Убыток


def cross_hedging(futures_price, spot_price, hedge_ratio, quantity):
    hedged_value = (futures_price - spot_price) * hedge_ratio * quantity
    return hedged_value


def volatility_trading(volatility_index, position_size, threshold):
    if volatility_index > threshold:  # threshold - заранее определенный уровень волатильности
        return position_size * volatility_index  # Потенциальная прибыль
    else:
        return 0  # Нет торговли


def pairs_trading(price_a, price_b, quantity, threshold):
    spread = price_a - price_b
    if spread > threshold:  # threshold - заранее определенный уровень спреда
        return (price_a - price_b) * quantity  # Потенциальная прибыль
    else:
        return 0  # Нет торговли


if __name__ == "__main__":
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
