import numpy as np
from scipy.stats import norm


def delta(S, K, T, r, sigma, option_type="call"):
    """
    Calculate the Delta of a European option.

    :param S: Current price of the underlying asset.
    :param K: Strike price of the option.
    :param T: Time to expiration (in years).
    :param r: Risk-free interest rate (annualized).
    :param sigma: Volatility of the underlying asset (annualized).
    :param option_type: Type of the option ("call" or "put").

    :return: Delta of the option.
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    if option_type == "call":
        return norm.cdf(d1)
    else:
        return norm.cdf(d1) - 1


def gamma(S, K, T, r, sigma):
    """
    Calculate the Gamma of a European option.

    :param S: Current price of the underlying asset.
    :param K: Strike price of the option.
    :param T: Time to expiration (in years).
    :param r: Risk-free interest rate (annualized).
    :param sigma: Volatility of the underlying asset (annualized).

    :return: Gamma of the option.
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    return norm.pdf(d1) / (S * sigma * np.sqrt(T))


def theta(S, K, T, r, sigma, option_type="call"):
    """
    Calculate the Theta of a European option.

    :param S: Current price of the underlying asset.
    :param K: Strike price of the option.
    :param T: Time to expiration (in years).
    :param r: Risk-free interest rate (annualized).
    :param sigma: Volatility of the underlying asset (annualized).
    :param option_type: Type of the option ("call" or "put").

    :return: Theta of the option.
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    first_term = - (S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T))

    if option_type == "call":
        second_term = - r * K * np.exp(-r * T) * norm.cdf(d2)
    else:
        second_term = r * K * np.exp(-r * T) * norm.cdf(-d2)

    return first_term + second_term


def vega(S, K, T, r, sigma):
    """
    Calculate the Vega of a European option.

    :param S: Current price of the underlying asset.
    :param K: Strike price of the option.
    :param T: Time to expiration (in years).
    :param r: Risk-free interest rate (annualized).
    :param sigma: Volatility of the underlying asset (annualized).

    :return: Vega of the option.
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    return S * norm.pdf(d1) * np.sqrt(T)


def rho(S, K, T, r, sigma, option_type="call"):
    """
    Calculate the Rho of a European option.

    :param S: Current price of the underlying asset.
    :param K: Strike price of the option.
    :param T: Time to expiration (in years).
    :param r: Risk-free interest rate (annualized).
    :param sigma: Volatility of the underlying asset (annualized).
    :param option_type: Type of the option ("call" or "put").

    :return: Rho of the option.
    """
    d2 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T)) - sigma * np.sqrt(T)

    if option_type == "call":
        return K * T * np.exp(-r * T) * norm.cdf(d2)
    else:
        return -K * T * np.exp(-r * T) * norm.cdf(-d2)


def greeks_summary(S, K, T, r, sigma, option_type="call"):
    """
    Generate a summary dictionary containing all Greeks for a European option.

    :param S: Current price of the underlying asset.
    :param K: Strike price of the option.
    :param T: Time to expiration (in years).
    :param r: Risk-free interest rate (annualized).
    :param sigma: Volatility of the underlying asset (annualized).
    :param option_type: Type of the option ("call" or "put").

    :return: Dictionary containing Delta, Gamma, Theta, Vega and Rho for the specified options.
    """
    return {
        "Delta": delta(S, K, T, r, sigma, option_type),
        "Gamma": gamma(S, K, T, r, sigma),
        "Theta": theta(S, K, T, r, sigma, option_type),
        "Vega": vega(S, K, T, r, sigma),
        "Rho": rho(S, K, T, r, sigma, option_type)
    }