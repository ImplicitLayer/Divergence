import numpy as np
from scipy.stats import norm


# Black-Scholes model
def black_scholes(S, K, T, r, sigma, option_type="call"):
    """
    Calculate option price using the Black-Scholes model.

    Parameters:
    S : float  -> Current stock price
    K : float  -> Strike price
    T : float  -> Time to expiration (in years)
    r : float  -> Risk-free interest rate (annualized)
    sigma : float  -> Volatility of the underlying asset
    option_type : str  -> "call" or "put"

    Returns:
    float: Option price
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == "call":
        return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == "put":
        return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("Invalid option type. Use 'call' or 'put'.")


# Binomial tree model
def binomial_tree(S, K, T, r, sigma, N, option_type="call"):
    """
    Calculate option price using the Binomial Tree model.
    """
    dt = T / N
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    p = (np.exp(r * dt) - d) / (u - d)

    option_values = np.maximum(0, (S * u ** np.arange(N, -1, -1) * d ** np.arange(0, N + 1) - K))

    for _ in range(N):
        option_values = np.exp(-r * dt) * (p * option_values[:-1] + (1 - p) * option_values[1:])

    return option_values[0] if option_type == "call" else np.maximum(0, K - option_values[0])


# Monte Carlo model
def monte_carlo(S, K, T, r, sigma, num_simulations=10000, option_type="call"):
    """
    Calculate option price using Monte Carlo simulation.
    """
    np.random.seed(42)
    Z = np.random.standard_normal(num_simulations)
    ST = S * np.exp((r - 0.5 * sigma ** 2) * T + sigma * np.sqrt(T) * Z)

    if option_type == "call":
        payoff = np.maximum(ST - K, 0)
    else:
        payoff = np.maximum(K - ST, 0)

    return np.exp(-r * T) * np.mean(payoff)


# Local volatility model (placeholder, needs surface interpolation)
def local_volatility(S, K, T, r, sigma_surface, option_type="call"):
    """
    Local volatility pricing using an interpolated volatility surface.

    Placeholder function. Requires a volatility surface model.
    """
    sigma = sigma_surface.get_volatility(S, T)  # Assume a callable object
    return black_scholes(S, K, T, r, sigma, option_type)


# Stochastic volatility model (Heston model placeholder)
def stochastic_volatility(S, K, T, r, v0, kappa, theta, sigma, rho, option_type="call"):
    """
    Stochastic volatility pricing using Heston model.

    Placeholder function. Requires numerical solution.
    """
    # Monte Carlo simulation for Heston Model (simplified)
    num_simulations = 10000
    dt = T / 100  # Time steps
    V = np.full(num_simulations, v0)
    S_sim = np.full(num_simulations, S)

    for _ in range(100):
        dW1 = np.random.randn(num_simulations) * np.sqrt(dt)
        dW2 = rho * dW1 + np.sqrt(1 - rho ** 2) * np.random.randn(num_simulations) * np.sqrt(dt)
        V = np.maximum(0, V + kappa * (theta - V) * dt + sigma * np.sqrt(V) * dW1)
        S_sim *= np.exp((r - 0.5 * V) * dt + np.sqrt(V) * dW2)

    if option_type == "call":
        payoff = np.maximum(S_sim - K, 0)
    else:
        payoff = np.maximum(K - S_sim, 0)

    return np.exp(-r * T) * np.mean(payoff)


# Example usage
if __name__ == "__main__":
    S, K, T, r, sigma = 100, 100, 1, 0.05, 0.2

    print("Black-Scholes Call Price:", black_scholes(S, K, T, r, sigma, "call"))
    print("Binomial Tree Call Price:", binomial_tree(S, K, T, r, sigma, 100, "call"))
    print("Monte Carlo Call Price:", monte_carlo(S, K, T, r, sigma, 10000, "call"))
