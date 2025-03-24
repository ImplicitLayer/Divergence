from divergence.options.pricing import black_scholes


def bull_call_spread(S, K1, K2, T, r, sigma, pricing_method):
    return pricing_method(S, K1, T, r, sigma, "call") - pricing_method(S, K2, T, r, sigma, "call")


def bear_put_spread(S, K1, K2, T, r, sigma, pricing_method):
    return pricing_method(S, K1, T, r, sigma, "put") - pricing_method(S, K2, T, r, sigma, "put")


def straddle(S, K, T, r, sigma, pricing_method):
    return pricing_method(S, K, T, r, sigma, "call") + pricing_method(S, K, T, r, sigma, "put")


def strangle(S, K1, K2, T, r, sigma, pricing_method):
    return pricing_method(S, K1, T, r, sigma, "call") + pricing_method(S, K2, T, r, sigma, "put")


def iron_condor(S, K1, K2, K3, K4, T, r, sigma, pricing_method):
    return (pricing_method(S, K1, T, r, sigma, "call") - pricing_method(S, K2, T, r, sigma, "call") +
            pricing_method(S, K3, T, r, sigma, "put") - pricing_method(S, K4, T, r, sigma, "put"))


def covered_call(S, K, T, r, sigma, pricing_method):
    return -pricing_method(S, K, T, r, sigma, "call") + S


if __name__ == "__main__":
    S, K, T, r, sigma = 100, 100, 1, 0.05, 0.2
    pricing_method = black_scholes  # Can be swapped with other pricing models

    print("Black-Scholes Call Price:", pricing_method(S, K, T, r, sigma, "call"))
    print("Bull Call Spread:", bull_call_spread(S, 95, 105, T, r, sigma, pricing_method))
    print("Bear Put Spread:", bear_put_spread(S, 95, 105, T, r, sigma, pricing_method))
    print("Straddle:", straddle(S, K, T, r, sigma, pricing_method))
    print("Strangle:", strangle(S, 95, 105, T, r, sigma, pricing_method))
    print("Iron Condor:", iron_condor(S, 90, 95, 105, 110, T, r, sigma, pricing_method))
    print("Covered Call:", covered_call(S, K, T, r, sigma, pricing_method))