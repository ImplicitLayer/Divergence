def bull_call_spread(S, K1, K2, T, r, sigma, pricing_method):
    """
    Calculate the profit from a bull call spread.

    :param S: Current price of the underlying asset.
    :param K1: Strike price of the first call option (long position).
    :param K2: Strike price of the second call option (short position).
    :param T: Time to expiration (in years).
    :param r: Risk-free interest rate (annualized).
    :param sigma: Volatility of the underlying asset (annualized).
    :param pricing_method: Function to calculate the option price.

    :return: Profit from the bull call spread.
    """
    return pricing_method(S, K1, T, r, sigma, "call") - pricing_method(S, K2, T, r, sigma, "call")


def bear_put_spread(S, K1, K2, T, r, sigma, pricing_method):
    """
    Calculate the profit from a bear put spread.

    :param S: Current price of the underlying asset.
    :param K1: Strike price of the first put option (long position).
    :param K2: Strike price of the second put option (short position).
    :param T: Time to expiration (in years).
    :param r: Risk-free interest rate (annualized).
    :param sigma: Volatility of the underlying asset (annualized).
    :param pricing_method: Function to calculate the option price.

    :return: Profit from the bear put spread.
    """
    return pricing_method(S, K1, T, r, sigma, "put") - pricing_method(S, K2, T, r, sigma, "put")


def straddle(S, K, T, r, sigma, pricing_method):
    """
    Calculate the profit from a straddle.

    :param S: Current price of the underlying asset.
    :param K: Strike price for both call and put options.
    :param T: Time to expiration (in years).
    :param r: Risk-free interest rate (annualized).
    :param sigma: Volatility of the underlying asset (annualized).
    :param pricing_method: Function to calculate the option price.

    :return: Profit from the straddle.
    """
    return pricing_method(S, K, T, r, sigma, "call") + pricing_method(S, K, T, r, sigma, "put")


def strangle(S, K1, K2, T, r, sigma, pricing_method):
    """
    Calculate the profit from a strangle.

    :param S: Current price of the underlying asset.
    :param K1: Strike price for the call option.
    :param K2: Strike price for the put option.
    :param T: Time to expiration (in years).
    :param r: Risk-free interest rate (annualized).
    :param sigma: Volatility of the underlying asset (annualized).
    :param pricing_method: Function to calculate the option price.

    :return: Profit from the strangle.
    """
    return pricing_method(S, K1, T, r, sigma, "call") + pricing_method(S, K2, T, r, sigma, "put")


def iron_condor(S, K1, K2, K3, K4, T, r, sigma, pricing_method):
    """
    Calculate the profit from an iron condor.

    :param S: Current price of the underlying asset.
    :param K1: Strike price for the first call option.
    :param K2: Strike price for the second call option.
    :param K3: Strike price for the first put option.
    :param K4: Strike price for the second put option.
    :param T: Time to expiration (in years).
    :param r: Risk-free interest rate (annualized).
    :param sigma: Volatility of the underlying asset (annualized).
    :param pricing_method: Function to calculate the option price.

    :return: Profit from the iron condor.
    """
    return (pricing_method(S, K1, T, r, sigma, "call") -
           pricing_method(S, K2, T, r, sigma, "call") +
           pricing_method(S, K3, T, r, sigma, "put") -
           pricing_method(S, K4, T, r, sigma, "put"))


def covered_call(S, K, T, r, sigma, pricing_method):
    """
    Calculate the profit from a covered call.

    :param S: Current price of the underlying asset.
    :param K: Strike price for the call option.
    :param T: Time to expiration (in years).
    :param r: Risk-free interest rate (annualized).
    :param sigma: Volatility of the underlying asset (annualized).
    :param pricing_method: Function to calculate the option price.

    :return: Profit from the covered call.
    """
    return -pricing_method(S, K, T, r, sigma, "call") + S
