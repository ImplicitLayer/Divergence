def calculate_commission(amount, commission_rate):
    """
    Calculate the commission based on the amount and commission rate.

    :param amount: The total amount on which the commission is calculated.
    :param commission_rate: The rate of the commission (as a decimal).
    :return: The calculated commission.
    """
    return amount * commission_rate


def direct_hedging(spot_price, futures_price, quantity, commission_rate):
    """
    Calculate profit or loss from direct hedging.

    :param spot_price: Current price of the asset.
    :param futures_price: Price of the futures contract.
    :param quantity: Quantity of the asset being hedged.
    :param commission_rate: The rate of the commission (as a decimal).
    :return: Net profit or loss after deducting commission.
    """
    profit_or_loss = (spot_price - futures_price) * quantity
    commission = calculate_commission(abs(profit_or_loss), commission_rate)
    return profit_or_loss - commission


def indirect_hedging(spot_price_a, futures_price_a, quantity_a, spot_price_b, futures_price_b, quantity_b, commission_rate):
    """
    Calculate profit or loss from indirect hedging involving two assets.

    :param spot_price_a: Current price of the first asset.
    :param futures_price_a: Price of the futures contract for the first asset.
    :param quantity_a: Quantity of the first asset being hedged.
    :param spot_price_b: Current price of the second asset.
    :param futures_price_b: Price of the futures contract for the second asset.
    :param quantity_b: Quantity of the second asset being hedged.
    :param commission_rate: The rate of the commission (as a decimal).
    :return: Net profit or loss after deducting commission from both assets.
    """
    profit_or_loss_a = (spot_price_a - futures_price_a) * quantity_a
    profit_or_loss_b = (spot_price_b - futures_price_b) * quantity_b
    total_profit_or_loss = profit_or_loss_a + profit_or_loss_b
    commission = calculate_commission(abs(total_profit_or_loss), commission_rate)
    return total_profit_or_loss - commission


def full_hedging(spot_price, futures_price, quantity, commission_rate):
    """
    Calculate profit or loss from full hedging.

    :param spot_price: Current price of the asset.
    :param futures_price: Price of the futures contract.
    :param quantity: Quantity of the asset being hedged.
    :param commission_rate: The rate of the commission (as a decimal).
    :return: Net profit or loss after deducting commission for full hedging.
    """
    futures_quantity = quantity / 100  # Предположим, что один фьючерсный контракт на 100 единиц
    profit_or_loss = -futures_price * futures_quantity
    commission = calculate_commission(abs(profit_or_loss), commission_rate)
    return profit_or_loss - commission


def partial_hedging(spot_price, futures_price, quantity, hedge_ratio, commission_rate):
    """
    Calculate profit or loss from partial hedging.

    :param spot_price: Current price of the asset.
    :param futures_price: Price of the futures contract.
    :param quantity: Quantity of the asset being hedged.
    :param hedge_ratio: Ratio indicating how much to hedge (between 0 and 1).
    :param commission_rate: The rate of the commission (as a decimal).
    :return: Net profit or loss after deducting commission for partial hedging.
    """
    futures_quantity = (quantity * hedge_ratio) / 100
    profit_or_loss = -futures_price * futures_quantity + (spot_price - futures_price) * quantity
    commission = calculate_commission(abs(profit_or_loss), commission_rate)
    return profit_or_loss - commission


def long_term_hedging(spot_price, futures_price, quantity, time_period, commission_rate):
    """
    Calculate profit or loss from long-term hedging.

    :param spot_price: Current price of the asset.
    :param futures_price: Price of the futures contract.
    :param quantity: Quantity of the asset being hedged.
    :param time_period: Time period over which to calculate profits/losses (in years).
    :param commission_rate: The rate of the commission (as a decimal).
    :return: Net profit or loss after deducting commissions for long-term hedging.
    """
    profit_or_loss = (spot_price - futures_price) * quantity * time_period
    commission = calculate_commission(abs(profit_or_loss), commission_rate)
    return profit_or_loss - commission


def short_term_hedging(spot_price, futures_price, quantity, time_period, commission_rate):
    """
    Calculate profit or loss from short-term hedging.

    :param spot_price: Current price of the asset.
    :param futures_price: Price of the futures contract.
    :param quantity: Quantity of the asset being hedged.
    :param time_period: Time period over which to calculate profits/losses (in years).
    :param commission_rate: The rate of the commission (as a decimal).
    :return: Net profit or loss after deducting commissions for short-term hedging.
    """
    profit_or_loss = (spot_price - futures_price) * quantity * time_period
    commission = calculate_commission(abs(profit_or_loss), commission_rate)
    return profit_or_loss - commission


def options_hedging(spot_price, option_price, quantity, commission_rate):
    """
    Calculate profit or loss from options hedging.

    :param spot_price: Current price of the underlying asset.
    :param option_price: Price paid for purchasing options contracts.
    :param quantity: Quantity of options contracts held/hedged.
    :param commission_rate: The rate of the commissions (as a decimal).
    :return: Net profit or loss after deducting commissions for options hedging.
    """
    profit_or_loss = (spot_price - option_price) * quantity
    commission = calculate_commission(abs(profit_or_loss), commission_rate)
    return profit_or_loss - commission


def cross_hedging(spot_price_a, futures_price_a, quantity_a, spot_price_b, futures_price_b, quantity_b, commission_rate):
    """
    Calculate profit or loss from cross-hedging involving two different assets.

    :param spot_price_a: Current price of the first asset.
    :param futures_price_a: Price of the futures contract for the first asset.
    :param quantity_a: Quantity of the first asset being hedged.
    :param spot_price_b: Current price of the second asset.
    :param futures_price_b: Price of the futures contract for the second asset.
    :param quantity_b: Quantity of the second asset being hedged.
    :param commission_rate: The rate of the commission (as a decimal).

    :return: Net profit or loss after deducting commission from both assets involved in cross-hedging.
    """
    profit_or_loss_a = (spot_price_a - futures_price_a) * quantity_a
    profit_or_loss_b = (spot_price_b - futures_price_b) * quantity_b
    total_profit_or_loss = profit_or_loss_a + profit_or_loss_b
    commission = calculate_commission(abs(total_profit_or_loss), commission_rate)
    return total_profit_or_loss - commission
