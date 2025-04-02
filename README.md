<div align="center">
  <img src="https://github.com/user-attachments/assets/4c6052f6-976c-41c7-9ad9-7baf7265dc28">
</div>
</br>

## Description
This project provides tools to analyze and work with different types of derivatives, including futures, options, swaps, as well as functions to evaluate the effectiveness of strategies.

## Structure
The module includes the following core files:

### 1. futures
Contains tools for working with futures, including:
- Futures pricing (calculating the value of a contract given the risk-free rate and time to execution).
- Futures hedging (methods of protecting against market risk using futures contracts).
- Futures trading strategies (spreads, arbitrage strategies and position combinations).

### 2. options
Includes:
- Option pricing (Black-Scholes, binomial model, Monte Carlo and other methods).
- Options Greeks (Delta, Gamma, Vega, Theta, Rho).
- Options hedging (Delta hedging, Gamma hedging, Vega hedging).
- Option strategies (spreads, straddles, strangles, Iron Condor, Covered Calls).

### 3. swaps
Allows analyzing different types of swaps:
- Interest rate swaps (fixed-to-floating, floating-to-floating).
- Currency swaps (exchange of payments in different currencies).
- Commodity swaps (hedging commodity price risks).
- Cash flow analysis (calculation of net contractual payments).

### 4. perfomance
Provides functions to evaluate the effectiveness of strategies:
- P&L (profit and loss) analysis.
- Comparison with benchmarks (SPX, bonds, volatility).
- Calculation of risk and volatility of strategies.

## Examples
The `examples/` folder contains examples of using all functions, including:
- futures_test.py - working with futures.
- options_test.py - calculating option prices, Greeks and strategies.
- swaps_test.py - analyze interest rate and currency swaps.
- perfomance_test.py - evaluation of trading strategies efficiency.

## Installation and use

### Installation

```bash 
git clone https://github.com/ImplicitLayer/Divergence.git
cd divergence
pip install -r requirements.txt
```

### Use
Example of delta hedging using the Black-Scholes model:
```python
from divergence.options.pricing import black_scholes
from divergence.options.hedging import delta_hedging

S, K, T, r, sigma = 100, 100, 1, 0.05, 0.2
portfolio_value = 100000
pricing_method = black_scholes

# Delta hedging
delta_hedge_position = delta_hedging(S, K, T, r, sigma, "call", portfolio_value, pricing_method)
print("Delta Hedge Position:", delta_hedge_position)

```

Example of calculating the price of a futures contract:
```python
from divergence.futures.pricing import calculate_gaussian_price

spot_price = 75 
volatility = 0.2
time_to_expiration = 1 

gaussian_price = calculate_gaussian_price(spot_price, volatility, time_to_expiration)
print(f"Price by Gaussian modeling: {gaussian_price:.2f}")
```

## Application
Designed to analyze and work with derivatives in trading and risk management.



