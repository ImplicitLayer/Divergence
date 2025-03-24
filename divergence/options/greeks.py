import numpy as np
from scipy.stats import norm


def delta(S, K, T, r, sigma, option_type="call"):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    if option_type == "call":
        return norm.cdf(d1)
    else:
        return norm.cdf(d1) - 1


def gamma(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    return norm.pdf(d1) / (S * sigma * np.sqrt(T))


def theta(S, K, T, r, sigma, option_type="call"):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    first_term = - (S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T))
    if option_type == "call":
        second_term = - r * K * np.exp(-r * T) * norm.cdf(d2)
    else:
        second_term = r * K * np.exp(-r * T) * norm.cdf(-d2)

    return first_term + second_term


def vega(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    return S * norm.pdf(d1) * np.sqrt(T)


def rho(S, K, T, r, sigma, option_type="call"):
    d2 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T)) - sigma * np.sqrt(T)
    if option_type == "call":
        return K * T * np.exp(-r * T) * norm.cdf(d2)
    else:
        return -K * T * np.exp(-r * T) * norm.cdf(-d2)


def greeks_summary(S, K, T, r, sigma, option_type="call"):
    return {
        "Delta": delta(S, K, T, r, sigma, option_type),
        "Gamma": gamma(S, K, T, r, sigma),
        "Theta": theta(S, K, T, r, sigma, option_type),
        "Vega": vega(S, K, T, r, sigma),
        "Rho": rho(S, K, T, r, sigma, option_type)
    }


# Example usage
if __name__ == "__main__":
    S, K, T, r, sigma = 100, 100, 1, 0.05, 0.2
    option_type = "call"

    print("Greeks Summary:")
    for greek, value in greeks_summary(S, K, T, r, sigma, option_type).items():
        print(f"{greek}: {value:.4f}")
