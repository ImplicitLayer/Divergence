from divergence.options.greeks import delta, gamma, vega
from divergence.options.pricing import black_scholes


def delta_hedging(S, K, T, r, sigma, option_type="call", portfolio_value=100000, pricing_method=None):
    # Calculate option price using pricing method
    option_price = pricing_method(S, K, T, r, sigma, option_type)

    # Calculate Delta of the option
    delta_value = delta(S, K, T, r, sigma, option_type)

    # Calculate the number of options to hedge the portfolio
    number_of_options = portfolio_value / option_price

    # Hedge position: Buy/Sell options to neutralize delta
    hedge_position = delta_value * number_of_options

    return hedge_position


def gamma_hedging(S, K, T, r, sigma, option_type="call", portfolio_value=100000, pricing_method=None):
    # Calculate option price using pricing method
    option_price = pricing_method(S, K, T, r, sigma, option_type)

    # Calculate Delta and Gamma of the option
    delta_value = delta(S, K, T, r, sigma, option_type)
    gamma_value = gamma(S, K, T, r, sigma)

    # Calculate the number of options to hedge the portfolio
    number_of_options = portfolio_value / option_price

    # Hedge position: Buy/Sell options to neutralize gamma
    hedge_position = gamma_value * number_of_options

    return hedge_position


def vega_hedging(S, K, T, r, sigma, option_type="call", portfolio_value=100000, pricing_method=None):
    # Calculate option price using pricing method
    option_price = pricing_method(S, K, T, r, sigma, option_type)

    # Calculate Vega of the option
    vega_value = vega(S, K, T, r, sigma)

    # Calculate the number of options to hedge the portfolio
    number_of_options = portfolio_value / option_price

    # Hedge position: Buy/Sell options to neutralize vega
    hedge_position = vega_value * number_of_options

    return hedge_position


def portfolio_hedging(S, K, T, r, sigma, option_type="call", portfolio_value=100000, pricing_method=None):
    # Calculate option price using pricing method
    option_price = pricing_method(S, K, T, r, sigma, option_type)

    # Calculate Greeks: Delta, Gamma, Vega for the option
    delta_value = delta(S, K, T, r, sigma, option_type)
    gamma_value = gamma(S, K, T, r, sigma)
    vega_value = vega(S, K, T, r, sigma)

    # Calculate the number of options to hedge the portfolio
    number_of_options = portfolio_value / option_price

    # Hedge position: Neutralize portfolio by combining the Greeks
    hedge_position = {
        "delta_hedge": delta_value * number_of_options,
        "gamma_hedge": gamma_value * number_of_options,
        "vega_hedge": vega_value * number_of_options
    }

    return hedge_position


# Example usage
if __name__ == "__main__":
    S, K, T, r, sigma = 100, 100, 1, 0.05, 0.2
    portfolio_value = 100000
    pricing_method = black_scholes  # You can change this to any other pricing method you like

    # Delta hedging
    delta_hedge_position = delta_hedging(S, K, T, r, sigma, "call", portfolio_value, pricing_method)
    print("Delta Hedge Position:", delta_hedge_position)

    # Gamma hedging
    gamma_hedge_position = gamma_hedging(S, K, T, r, sigma, "call", portfolio_value, pricing_method)
    print("Gamma Hedge Position:", gamma_hedge_position)

    # Vega hedging
    vega_hedge_position = vega_hedging(S, K, T, r, sigma, "call", portfolio_value, pricing_method)
    print("Vega Hedge Position:", vega_hedge_position)

    # Portfolio hedging
    portfolio_hedge_position = portfolio_hedging(S, K, T, r, sigma, "call", portfolio_value, pricing_method)
    print("Portfolio Hedge Position:")
    for hedge_type, position in portfolio_hedge_position.items():
        print(f"{hedge_type}: {position}")
