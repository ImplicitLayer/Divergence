import math
from scipy.stats import norm


def calculate_kaplan_sharpe_price(spot_price, strike_price, risk_free_rate, time_to_expiration):
    """
    Calculation of the futures contract price using the Kaplan-Sharpe model.

    :param spot_price: Current price of the asset.
    :param strike_price: Strike price.
    :param risk_free_rate: Risk-free rate.
    :param time_to_expiration: Time until contract expiration (in years).
    :return: Estimated price of the futures contract.
    """
    return spot_price * math.exp(risk_free_rate * time_to_expiration)


def calculate_cost_of_carry_price(spot_price, storage_cost, risk_free_rate, time_to_expiration, dividends=0):
    """
    Calculation of the futures contract price using the storage cost model.

    :param spot_price: Current price of the asset.
    :param storage_cost: Storage cost.
    :param risk_free_rate: Risk-free rate.
    :param time_to_expiration: Time until contract expiration (in years).
    :param dividends: Dividends (default is 0).
    :return: Estimated price of the futures contract.
    """
    return spot_price + storage_cost * time_to_expiration - dividends * math.exp(-risk_free_rate * time_to_expiration)


def calculate_hanna_price(spot_price, demand_factor, supply_factor):
    """
    Calculation of the futures contract price using the Hanna model.

    :param spot_price: Current price of the asset.
    :param demand_factor: Demand factor.
    :param supply_factor: Supply factor.
    :return: Estimated price of the futures contract.
    """
    return spot_price * (1 + demand_factor - supply_factor)


def calculate_gaussian_price(spot_price, volatility, time_to_expiration):
    """
    Calculation of the futures contract price using the Gaussian model.

    :param spot_price: Current price of the asset.
    :param volatility: Volatility of the asset.
    :param time_to_expiration: Time until contract expiration (in years).
    :return: Estimated price of the futures contract.
    """
    mean_price = spot_price
    std_dev = volatility * math.sqrt(time_to_expiration)
    return mean_price + std_dev * norm.ppf(0.5)
