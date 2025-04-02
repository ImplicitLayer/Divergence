def buy_and_hold(prices, initial_investment):
    """
    Calculate the final value of an investment using a buy-and-hold strategy.

    :param prices: A list of prices for the asset over time.
    :param initial_investment: The initial amount of money invested.

    :return: The final value of the investment after holding until the last price.
    """
    shares = initial_investment / prices[0]  # Количество акций, которые можно купить
    final_value = shares * prices[-1]  # Конечная стоимость
    return final_value


def arbitrage(price_a, price_b, quantity):
    """
    Calculate potential profit from arbitrage between two assets.

    :param price_a: Price of the first asset.
    :param price_b: Price of the second asset.
    :param quantity: Quantity of assets involved in the arbitrage.

    :return: Profit from arbitrage if possible; otherwise, returns 0.
    """
    if price_a < price_b:
        profit = (price_b - price_a) * quantity
        return profit
    else:
        return 0  # Нет возможности для арбитража


def short_selling(initial_price, final_price, quantity):
    """
    Calculate profit or loss from short selling an asset.

    :param initial_price: Price at which the asset was sold short.
    :param final_price: Price at which the asset is bought back.
    :param quantity: Quantity of assets sold short.

    :return: Profit from short selling if successful; otherwise, returns a negative loss.
    """
    if final_price < initial_price:
        profit = (initial_price - final_price) * quantity
        return profit
    else:
        loss = (final_price - initial_price) * quantity
        return -loss  # Убыток


def cross_hedging(futures_price, spot_price, hedge_ratio, quantity):
    """
    Calculate the hedged value from cross-hedging between futures and spot prices.

    :param futures_price: Price of the futures contract.
    :param spot_price: Current spot price of the asset.
    :param hedge_ratio: Ratio used for hedging (how much to hedge).
    :param quantity: Quantity of assets being hedged.

    :return: Value derived from cross-hedging based on futures and spot prices.
    """
    hedged_value = (futures_price - spot_price) * hedge_ratio * quantity
    return hedged_value


def volatility_trading(volatility_index, position_size, threshold):
    """
    Determine potential profit from trading based on volatility levels.

    :param volatility_index: Current index measuring market volatility.
    :param position_size: Size of the trading position taken based on volatility.
    :param threshold: Predefined level of volatility to trigger trading.

    :return: Potential profit if volatility exceeds threshold; otherwise, returns 0.
    """
    if volatility_index > threshold:  # threshold - заранее определенный уровень волатильности
        return position_size * volatility_index  # Потенциальная прибыль
    else:
        return 0  # Нет торговли


def pairs_trading(price_a, price_b, quantity, threshold):
    """
    Calculate potential profit from pairs trading based on price spread.

    :param price_a: Price of the first asset in the pair.
    :param price_b: Price of the second asset in the pair.
    :param quantity: Quantity of assets involved in pairs trading.
    :param threshold: Predefined level for spread to trigger trading.

    :return: Potential profit if spread exceeds threshold; otherwise, returns 0.
    """
    spread = price_a - price_b
    if spread > threshold:  # threshold - заранее определенный уровень спреда
        return (price_a - price_b) * quantity  # Потенциальная прибыль
    else:
        return 0  # Нет торговли
