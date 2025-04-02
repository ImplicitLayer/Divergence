class InterestRateSwapValuation:
    def __init__(self, notional, fixed_rate, floating_rate, payment_frequency, years_to_maturity):
        """
        Initializes the Interest Rate Swap Valuation.

        :param notional: The principal amount of the swap.
        :param fixed_rate: The fixed interest rate paid by one party.
        :param floating_rate: The floating interest rate received by one party.
        :param payment_frequency: The number of payments per year (e.g., 1 for annual, 2 for semi-annual).
        :param years_to_maturity: The total duration of the swap in years.
        """
        self.notional = notional
        self.fixed_rate = fixed_rate
        self.floating_rate = floating_rate
        self.payment_frequency = payment_frequency
        self.years_to_maturity = years_to_maturity

    def present_value_fixed_leg(self, market_rate):
        """
        Calculates the present value of the fixed leg of the swap.

        :param market_rate: The market interest rate used for discounting.
        :return: The present value of the fixed leg.
        """
        fixed_payment = self.notional * self.fixed_rate / self.payment_frequency
        total_pv = 0

        for t in range(1, self.years_to_maturity * self.payment_frequency + 1):
            discount_factor = 1 / (1 + market_rate / self.payment_frequency) ** t
            total_pv += fixed_payment * discount_factor

        return total_pv

    def present_value_floating_leg(self, market_rate):
        """
        Calculates the present value of the floating leg of the swap.

        :param market_rate: The market interest rate used for discounting.
        :return: The present value of the floating leg.
        """
        floating_payment = self.notional * self.floating_rate / self.payment_frequency
        total_pv = 0

        for t in range(1, self.years_to_maturity * self.payment_frequency + 1):
            discount_factor = 1 / (1 + market_rate / self.payment_frequency) ** t
            total_pv += floating_payment * discount_factor

        return total_pv

    def net_present_value(self, market_rate):
        """
        Calculates the net present value (NPV) of the interest rate swap.

        :param market_rate: The market interest rate used for discounting.
        :return: The net present value of the swap (PV_fixed - PV_floating).
        """
        pv_fixed = self.present_value_fixed_leg(market_rate)
        pv_floating = self.present_value_floating_leg(market_rate)

        return pv_fixed - pv_floating


class CurrencySwapValuation:
    def __init__(self, notional_a, notional_b, fixed_rate_a, fixed_rate_b, payment_frequency, years_to_maturity):
        """
        Initializes the Currency Swap Valuation.

        :param notional_a: The principal amount in currency A.
        :param notional_b: The principal amount in currency B.
        :param fixed_rate_a: The fixed interest rate for currency A.
        :param fixed_rate_b: The fixed interest rate for currency B.
        :param payment_frequency: The number of payments per year (e.g., 1 for annual, 2 for semi-annual).
        :param years_to_maturity: The total duration of the swap in years.
        """
        self.notional_a = notional_a
        self.notional_b = notional_b
        self.fixed_rate_a = fixed_rate_a
        self.fixed_rate_b = fixed_rate_b
        self.payment_frequency = payment_frequency
        self.years_to_maturity = years_to_maturity

    def present_value_fixed_leg_a(self, market_rate_a):
        """
        Calculates the present value of the fixed leg for currency A.

        :param market_rate_a: The market interest rate used for discounting currency A's cash flows.
        :return: The present value of the fixed leg for currency A.
        """
        fixed_payment_a = self.notional_a * self.fixed_rate_a / self.payment_frequency
        total_pv_a = 0

        for t in range(1, self.years_to_maturity * self.payment_frequency + 1):
            discount_factor_a = 1 / (1 + market_rate_a / self.payment_frequency) ** t
            total_pv_a += fixed_payment_a * discount_factor_a

        return total_pv_a

    def present_value_fixed_leg_b(self, market_rate_b):
        """
        Calculates the present value of the fixed leg for currency B.

        :param market_rate_b: The market interest rate used for discounting currency B's cash flows.
        :return: The present value of the fixed leg for currency B.
        """
        fixed_payment_b = self.notional_b * self.fixed_rate_b / self.payment_frequency
        total_pv_b = 0

        for t in range(1, self.years_to_maturity * self.payment_frequency + 1):
            discount_factor_b = 1 / (1 + market_rate_b / self.payment_frequency) ** t
            total_pv_b += fixed_payment_b * discount_factor_b

        return total_pv_b

    def net_present_value(self, market_rate_a, market_rate_b):
        """
        Calculates the net present value (NPV) of the currency swap.

        :param market_rate_a: The market interest rate used for discounting currency A's cash flows.
        :param market_rate_b: The market interest rate used for discounting currency B's cash flows.
        :return: The net present value of the swap (PV_fixed_A - PV_fixed_B).
        """
        pv_fixed_a = self.present_value_fixed_leg_a(market_rate_a)
        pv_fixed_b = self.present_value_fixed_leg_b(market_rate_b)

        return pv_fixed_a - pv_fixed_b


class CommoditySwapValuation:
    def __init__(self, notional, fixed_price, floating_price, payment_frequency, years_to_maturity):
        """
        Initializes the Commodity Swap Valuation.

        :param notional: The principal amount of the commodity swap.
        :param fixed_price: The agreed-upon price to be paid in each period.
        :param floating_price: The variable price received based on current market conditions.
        :param payment_frequency: The number of payments per year (e.g., 1 for annual, 2 for semi-annual).
        :param years_to_maturity: The total duration of the swap in years.
        """
        self.notional = notional
        self.fixed_price = fixed_price
        self.floating_price = floating_price
        self.payment_frequency = payment_frequency
        self.years_to_maturity = years_to_maturity

    def present_value_fixed_leg(self, market_price):
        """
        Calculates the present value of the fixed leg based on a predetermined price.

        :param market_price: Current price used to calculate cash flows and discounts.
        :return: Present value of cash flows from the fixed leg.
        """
        fixed_payment = self.notional * self.fixed_price / self.payment_frequency
        total_pv = 0

        for t in range(1, self.years_to_maturity * self.payment_frequency + 1):
            discount_factor = 1 / (1 + market_price / self.payment_frequency) ** t
            total_pv += fixed_payment * discount_factor

        return total_pv

    def present_value_floating_leg(self, market_price):
        """
        Calculates the present value of the floating leg based on current prices.

        :param market_price: Current price used to calculate cash flows and discounts.
        :return: Present value of cash flows from the floating leg.
        """
        floating_payment = self.notional * self.floating_price / self.payment_frequency
        total_pv = 0

        for t in range(1, self.years_to_maturity * self.payment_frequency + 1):
            discount_factor = 1 / (1 + market_price / self.payment_frequency) ** t
            total_pv += floating_payment * discount_factor

        return total_pv

    def net_present_value(self, market_price):
        """
        Calculates the net present value (NPV) of the commodity swap.

        :param market_price: Current price used to calculate cash flows and discounts.
        :return: Net present value calculated as PV_fixed - PV_floating.
        """
        pv_fixed = self.present_value_fixed_leg(market_price)
        pv_floating = self.present_value_floating_leg(market_price)

        return pv_fixed - pv_floating
