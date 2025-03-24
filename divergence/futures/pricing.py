import math
from scipy.stats import norm


def calculate_kaplan_sharpe_price(spot_price, strike_price, risk_free_rate, time_to_expiration):
    """Расчет цены фьючерсного контракта по модели Каплана-Шарпа.

    :param spot_price: Текущая цена актива.
    :param strike_price: Цена исполнения.
    :param risk_free_rate: Безрисковая ставка.
    :param time_to_expiration: Время до истечения контракта (в годах).
    :return: Оцененная цена фьючерсного контракта.
    """
    return spot_price * math.exp(risk_free_rate * time_to_expiration)


def calculate_cost_of_carry_price(spot_price, storage_cost, risk_free_rate, time_to_expiration, dividends=0):
    """Расчет цены фьючерсного контракта по модели стоимости хранения.

    :param spot_price: Текущая цена актива.
    :param storage_cost: Стоимость хранения.
    :param risk_free_rate: Безрисковая ставка.
    :param time_to_expiration: Время до истечения контракта (в годах).
    :param dividends: Дивиденды (по умолчанию 0).
    :return: Оцененная цена фьючерсного контракта.
    """
    return spot_price + storage_cost * time_to_expiration - dividends * math.exp(-risk_free_rate * time_to_expiration)


def calculate_hanna_price(spot_price, demand_factor, supply_factor):
    """Расчет цены фьючерсного контракта по модели Ханна.

    :param spot_price: Текущая цена актива.
    :param demand_factor: Фактор спроса.
    :param supply_factor: Фактор предложения.
    :return: Оцененная цена фьючерсного контракта.
    """
    return spot_price * (1 + demand_factor - supply_factor)


def calculate_gaussian_price(spot_price, volatility, time_to_expiration):
    """Расчет цены фьючерсного контракта по модели Гаусса.

    :param spot_price: Текущая цена актива.
    :param volatility: Волатильность актива.
    :param time_to_expiration: Время до истечения контракта (в годах).
    :return: Оцененная цена фьючерсного контракта.
    """
    mean_price = spot_price
    std_dev = volatility * math.sqrt(time_to_expiration)
    return mean_price + std_dev * norm.ppf(0.5)  # Используем 0.5 для оценки средней цены


def main():
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


if __name__ == "__main__":
    main()