class InterestRateSwap:
    def __init__(self, notional, fixed_rate, floating_rate, payment_frequency, years_to_maturity):
        self.notional = notional
        self.fixed_rate = fixed_rate
        self.floating_rate = floating_rate
        self.payment_frequency = payment_frequency
        self.years_to_maturity = years_to_maturity

    def present_value_fixed_leg(self, market_rate):
        fixed_payment = self.notional * self.fixed_rate / self.payment_frequency
        total_pv = 0
        for t in range(1, self.years_to_maturity * self.payment_frequency + 1):
            discount_factor = 1 / (1 + market_rate / self.payment_frequency) ** t
            total_pv += fixed_payment * discount_factor
        return total_pv

    def present_value_floating_leg(self, market_rate):
        floating_payment = self.notional * self.floating_rate / self.payment_frequency
        total_pv = 0
        for t in range(1, self.years_to_maturity * self.payment_frequency + 1):
            discount_factor = 1 / (1 + market_rate / self.payment_frequency) ** t
            total_pv += floating_payment * discount_factor
        return total_pv

    def net_present_value(self, market_rate):
        pv_fixed = self.present_value_fixed_leg(market_rate)
        pv_floating = self.present_value_floating_leg(market_rate)
        return pv_fixed - pv_floating


class CurrencySwap:
    def __init__(self, notional_a, notional_b, fixed_rate_a, fixed_rate_b, payment_frequency, years_to_maturity):
        self.notional_a = notional_a
        self.notional_b = notional_b
        self.fixed_rate_a = fixed_rate_a
        self.fixed_rate_b = fixed_rate_b
        self.payment_frequency = payment_frequency
        self.years_to_maturity = years_to_maturity

    def present_value_fixed_leg_a(self, market_rate_a):
        fixed_payment_a = self.notional_a * self.fixed_rate_a / self.payment_frequency
        total_pv_a = 0
        for t in range(1, self.years_to_maturity * self.payment_frequency + 1):
            discount_factor_a = 1 / (1 + market_rate_a / self.payment_frequency) ** t
            total_pv_a += fixed_payment_a * discount_factor_a
        return total_pv_a

    def present_value_fixed_leg_b(self, market_rate_b):
        fixed_payment_b = self.notional_b * self.fixed_rate_b / self.payment_frequency
        total_pv_b = 0
        for t in range(1, self.years_to_maturity * self.payment_frequency + 1):
            discount_factor_b = 1 / (1 + market_rate_b / self.payment_frequency) ** t
            total_pv_b += fixed_payment_b * discount_factor_b
        return total_pv_b

    def net_present_value(self, market_rate_a, market_rate_b):
        pv_fixed_a = self.present_value_fixed_leg_a(market_rate_a)
        pv_fixed_b = self.present_value_fixed_leg_b(market_rate_b)
        return pv_fixed_a - pv_fixed_b


class CommoditySwap:
    def __init__(self, notional, fixed_price, floating_price, payment_frequency, years_to_maturity):
        self.notional = notional
        self.fixed_price = fixed_price
        self.floating_price = floating_price
        self.payment_frequency = payment_frequency
        self.years_to_maturity = years_to_maturity

    def present_value_fixed_leg(self, market_price):
        fixed_payment = self.notional * self.fixed_price / self.payment_frequency
        total_pv = 0
        for t in range(1, self.years_to_maturity * self.payment_frequency + 1):
            discount_factor = 1 / (1 + market_price / self.payment_frequency) ** t
            total_pv += fixed_payment * discount_factor
        return total_pv

    def present_value_floating_leg(self, market_price):
        floating_payment = self.notional * self.floating_price / self.payment_frequency
        total_pv = 0
        for t in range(1, self.years_to_maturity * self.payment_frequency + 1):
            discount_factor = 1 / (1 + market_price / self.payment_frequency) ** t
            total_pv += floating_payment * discount_factor
        return total_pv

    def net_present_value(self, market_price):
        pv_fixed = self.present_value_fixed_leg(market_price)
        pv_floating = self.present_value_floating_leg(market_price)
        return pv_fixed - pv_floating


if __name__ == "__main__":
    # Оценка процентного свопа
    swap = InterestRateSwap(notional=1000000, fixed_rate=0.03, floating_rate=0.025, payment_frequency=2, years_to_maturity=5)
    market_rate = 0.02
    npv = swap.net_present_value(market_rate)
    print(f"Чистая текущая стоимость процентного свопа: {npv:.2f}")

    # Оценка валютного свопа
    currency_swap = CurrencySwap(notional_a=1000000, notional_b=800000, fixed_rate_a=0.02, fixed_rate_b=0.025, payment_frequency=2, years_to_maturity=5)
    market_rate_a = 0.015
    market_rate_b = 0.02
    npv_currency = currency_swap.net_present_value(market_rate_a, market_rate_b)
    print(f"Чистая текущая стоимость валютного свопа: {npv_currency:.2f}")

    # Оценка товарного свопа
    commodity_swap = CommoditySwap(notional=1000, fixed_price=50, floating_price=55, payment_frequency=2, years_to_maturity=5)
    market_price = 52
    npv_commodity = commodity_swap.net_present_value(market_price)
    print(f"Чистая текущая стоимость товарного свопа: {npv_commodity:.2f}")