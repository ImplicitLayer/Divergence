class Swap:
    def __init__(self, notional, payment_frequency, maturity):
        """
        Initializes a basic swap.

        :param notional: The notional amount of the swap (principal).
        :param payment_frequency: The frequency of payments (e.g., 1 for annual, 2 for semi-annual).
        :param maturity: The term of the swap in years.
        """
        self.notional = notional
        self.payment_frequency = payment_frequency
        self.maturity = maturity

    def present_value(self, cash_flows, discount_rate):
        """
        Calculates the present value of cash flows.

        :param cash_flows: A list of cash flows.
        :param discount_rate: The discount rate.
        :return: The present value of the cash flows.
        """
        pv = sum(cf / (1 + discount_rate) ** i for i, cf in enumerate(cash_flows, start=1))
        return pv


class InterestRateSwap(Swap):
    def __init__(self, notional, fixed_rate, payment_frequency, maturity):
        """
        Initializes an interest rate swap.

        :param notional: The notional amount of the swap (principal).
        :param fixed_rate: The fixed interest rate for the swap.
        :param payment_frequency: The frequency of payments (e.g., 1 for annual, 2 for semi-annual).
        :param maturity: The term of the swap in years.
        """
        super().__init__(notional, payment_frequency, maturity)
        self.fixed_rate = fixed_rate

    def calculate_fixed_cash_flows(self):
        """
        Calculates the fixed cash flows for the interest rate swap.

        :return: A list of fixed cash flows.
        """
        cash_flows = []
        for i in range(1, self.maturity * self.payment_frequency + 1):
            cash_flows.append(self.notional * self.fixed_rate / self.payment_frequency)
        return cash_flows

    def calculate_floating_cash_flows(self, floating_rates):
        """
        Calculates the floating cash flows based on provided floating rates.

        :param floating_rates: A list of floating interest rates.
        :return: A list of floating cash flows.
        """
        cash_flows = []
        for rate in floating_rates:
            cash_flows.append(self.notional * rate / self.payment_frequency)
        return cash_flows

    def swap_value(self, floating_rates, discount_rate):
        """
        Calculates the net present value of the interest rate swap.

        :param floating_rates: A list of floating interest rates.
        :param discount_rate: The discount rate.
        :return: The net present value of the swap.
        """
        fixed_cash_flows = self.calculate_fixed_cash_flows()
        floating_cash_flows = self.calculate_floating_cash_flows(floating_rates)

        pv_fixed = self.present_value(fixed_cash_flows, discount_rate)
        pv_floating = self.present_value(floating_cash_flows, discount_rate)

        return pv_floating - pv_fixed


class CurrencySwap(Swap):
    def __init__(self, notional_a, notional_b, fixed_rate_a, fixed_rate_b, payment_frequency, maturity):
        """
        Initializes a currency swap.

        :param notional_a: The notional amount in currency A.
        :param notional_b: The notional amount in currency B.
        :param fixed_rate_a: The fixed interest rate for currency A.
        :param fixed_rate_b: The fixed interest rate for currency B.
        :param payment_frequency: The frequency of payments (e.g., 1 for annual, 2 for semi-annual).
        :param maturity: The term of the swap in years.
        """
        super().__init__(notional_a, payment_frequency, maturity)
        self.notional_a = notional_a
        self.notional_b = notional_b
        self.fixed_rate_a = fixed_rate_a
        self.fixed_rate_b = fixed_rate_b

    def calculate_fixed_cash_flows_a(self):
        """
        Calculates the fixed cash flows for currency A.

        :return: A list of fixed cash flows for currency A.
        """
        cash_flows = []
        for i in range(1, self.maturity * self.payment_frequency + 1):
            cash_flows.append(self.notional_a * self.fixed_rate_a / self.payment_frequency)
        return cash_flows

    def calculate_fixed_cash_flows_b(self):
        """
        Calculates the fixed cash flows for currency B.

        :return: A list of fixed cash flows for currency B.
        """
        cash_flows = []
        for i in range(1, self.maturity * self.payment_frequency + 1):
            cash_flows.append(self.notional_b * self.fixed_rate_b / self.payment_frequency)
        return cash_flows

    def swap_value(self, discount_rate):
        """
        Calculates the net present value of the currency swap.

        :param discount_rate: The discount rate.
        :return: The net present value of the currency swap.
        """
        cash_flows_a = self.calculate_fixed_cash_flows_a()
        cash_flows_b = self.calculate_fixed_cash_flows_b()

        pv_a = self.present_value(cash_flows_a, discount_rate)
        pv_b = self.present_value(cash_flows_b, discount_rate)

        return pv_a - pv_b


class CommoditySwap(Swap):
    def __init__(self, notional, fixed_price, payment_frequency, maturity):
        """
        Initializes a commodity swap.

        :param notional: The notional amount of the swap (principal).
        :param fixed_price: The fixed price agreed upon in the commodity swap.
        :param payment_frequency: The frequency of payments (e.g., 1 for annual, 2 for semi-annual).
        :param maturity: The term of the swap in years.
        """
        super().__init__(notional, payment_frequency, maturity)
        self.fixed_price = fixed_price

    def calculate_fixed_cash_flows(self):
        """
        Calculates the fixed cash flows based on a predetermined price.

        :return: A list of fixed cash flows based on the agreed price.
        """
        cash_flows = []
        for i in range(1, self.maturity * self.payment_frequency + 1):
            cash_flows.append(self.notional * self.fixed_price / self.payment_frequency)
        return cash_flows

    def calculate_floating_cash_flows(self, floating_prices):
        """
        Calculates the floating cash flows based on provided market prices.

        :param floating_prices: A list of market prices at each payment period.
        :return: A list of floating cash flows based on market prices.
        """
        cash_flows = []
        for price in floating_prices:
            cash_flows.append(self.notional * price / self.payment_frequency)
        return cash_flows

    def swap_value(self, floating_prices, discount_rate):
        """
        Calculates the net present value of the commodity swap.

        :param floating_prices: A list of market prices at each payment period.
        :param discount_rate: The discount rate used to calculate present values.
        :return: The net present value of the commodity swap.
        """
        fixed_cash_flows = self.calculate_fixed_cash_flows()
        floating_cash_flows = self.calculate_floating_cash_flows(floating_prices)

        pv_fixed = self.present_value(fixed_cash_flows, discount_rate)
        pv_floating = self.present_value(floating_cash_flows, discount_rate)

        return pv_floating - pv_fixed
