def calculate_commission(amount, commission_rate):
    return amount * commission_rate


def direct_hedging(spot_price, futures_price, quantity, commission_rate):
    profit_or_loss = (spot_price - futures_price) * quantity
    commission = calculate_commission(abs(profit_or_loss), commission_rate)
    return profit_or_loss - commission


def indirect_hedging(spot_price_a, futures_price_a, quantity_a, spot_price_b, futures_price_b, quantity_b, commission_rate):
    profit_or_loss_a = (spot_price_a - futures_price_a) * quantity_a
    profit_or_loss_b = (spot_price_b - futures_price_b) * quantity_b
    total_profit_or_loss = profit_or_loss_a + profit_or_loss_b
    commission = calculate_commission(abs(total_profit_or_loss), commission_rate)
    return total_profit_or_loss - commission


def full_hedging(spot_price, futures_price, quantity, commission_rate):
    futures_quantity = quantity / 100  # Предположим, что один фьючерсный контракт на 100 единиц
    profit_or_loss = -futures_price * futures_quantity
    commission = calculate_commission(abs(profit_or_loss), commission_rate)
    return profit_or_loss - commission


def partial_hedging(spot_price, futures_price, quantity, hedge_ratio, commission_rate):
    futures_quantity = (quantity * hedge_ratio) / 100
    profit_or_loss = -futures_price * futures_quantity + (spot_price - futures_price) * quantity
    commission = calculate_commission(abs(profit_or_loss), commission_rate)
    return profit_or_loss - commission


def long_term_hedging(spot_price, futures_price, quantity, time_period, commission_rate):
    profit_or_loss = (spot_price - futures_price) * quantity * time_period
    commission = calculate_commission(abs(profit_or_loss), commission_rate)
    return profit_or_loss - commission


def short_term_hedging(spot_price, futures_price, quantity, time_period, commission_rate):
    profit_or_loss = (spot_price - futures_price) * quantity * time_period
    commission = calculate_commission(abs(profit_or_loss), commission_rate)
    return profit_or_loss - commission


def options_hedging(spot_price, option_price, quantity, commission_rate):
    profit_or_loss = (spot_price - option_price) * quantity
    commission = calculate_commission(abs(profit_or_loss), commission_rate)
    return profit_or_loss - commission


def cross_hedging(spot_price_a, futures_price_a, quantity_a, spot_price_b, futures_price_b, quantity_b, commission_rate):
    profit_or_loss_a = (spot_price_a - futures_price_a) * quantity_a
    profit_or_loss_b = (spot_price_b - futures_price_b) * quantity_b
    total_profit_or_loss = profit_or_loss_a + profit_or_loss_b
    commission = calculate_commission(abs(total_profit_or_loss), commission_rate)
    return total_profit_or_loss - commission


if __name__ == "__main__":
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
    print("Косвенное хеджирование:", indirect_hedging(spot_price_a, futures_price_a, quantity_a, spot_price_b, futures_price_b, quantity_b, commission_rate))
    print("Полное хеджирование:", full_hedging(spot_price_a, futures_price_a, quantity_a, commission_rate))
    print("Частичное хеджирование (50%):", partial_hedging(spot_price_a, futures_price_a, quantity_a, hedge_ratio=0.5, commission_rate=commission_rate))
    print("Долгосрочное хеджирование (12 месяцев):", long_term_hedging(spot_price_a, futures_price_a, quantity_a, time_period=12, commission_rate=commission_rate))
    print("Краткосрочное хеджирование (1 месяц):", short_term_hedging(spot_price_a, futures_price_a, quantity_a, time_period=1, commission_rate=commission_rate))
    print("Хеджирование с использованием опционов:", options_hedging(spot_price_a, 90, quantity_a, commission_rate))
    print("Кросс-хеджирование:", cross_hedging(spot_price_a, futures_price_a, quantity_a, spot_price_b, futures_price_b, quantity_b, commission_rate))
