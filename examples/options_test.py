from divergence.options.greeks import *
from divergence.options.hedging import *
from divergence.options.pricing import *
from divergence.options.strategies import *

# Greeks
S, K, T, r, sigma = 100, 100, 1, 0.05, 0.2
option_type = "call"

print("Greeks Summary:")
for greek, value in greeks_summary(S, K, T, r, sigma, option_type).items():
    print(f"{greek}: {value:.4f}")

# Hedging
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


# pricing
S, K, T, r, sigma = 100, 100, 1, 0.05, 0.2

print("Black-Scholes Call Price:", black_scholes(S, K, T, r, sigma, "call"))
print("Binomial Tree Call Price:", binomial_tree(S, K, T, r, sigma, 100, "call"))
print("Monte Carlo Call Price:", monte_carlo(S, K, T, r, sigma, 10000, "call"))


# strategies
S, K, T, r, sigma = 100, 100, 1, 0.05, 0.2
pricing_method = black_scholes  # Can be swapped with other pricing models

print("Black-Scholes Call Price:", pricing_method(S, K, T, r, sigma, "call"))
print("Bull Call Spread:", bull_call_spread(S, 95, 105, T, r, sigma, pricing_method))
print("Bear Put Spread:", bear_put_spread(S, 95, 105, T, r, sigma, pricing_method))
print("Straddle:", straddle(S, K, T, r, sigma, pricing_method))
print("Strangle:", strangle(S, 95, 105, T, r, sigma, pricing_method))
print("Iron Condor:", iron_condor(S, 90, 95, 105, 110, T, r, sigma, pricing_method))
print("Covered Call:", covered_call(S, K, T, r, sigma, pricing_method))

