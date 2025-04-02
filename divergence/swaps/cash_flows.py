class CashFlow:
    def __init__(self, amount, time_period):
        """
        Initializes a cash flow.

        :param amount: The amount of the cash flow.
        :param time_period: The time period when the cash flow occurs (in years).
        """
        self.amount = amount
        self.time_period = time_period

    def present_value(self, discount_rate):
        """
        Calculates the present value of the cash flow.

        :param discount_rate: The discount rate.
        :return: The present value of the cash flow.
        """
        return self.amount / (1 + discount_rate) ** self.time_period


class CashFlowSeries:
    def __init__(self):
        """Initializes a series of cash flows."""
        self.cash_flows = []

    def add_cash_flow(self, cash_flow):
        """
        Adds a cash flow to the series.

        :param cash_flow: A CashFlow object.
        """
        self.cash_flows.append(cash_flow)

    def total_present_value(self, discount_rate):
        """
        Calculates the total present value of all cash flows in the series.

        :param discount_rate: The discount rate.
        :return: The total present value.
        """
        total_pv = sum(cf.present_value(discount_rate) for cf in self.cash_flows)
        return total_pv

    def __str__(self):
        """Returns a string representation of the series of cash flows."""
        return "\n".join(f"Cash Flow: {cf.amount} at time {cf.time_period}" for cf in self.cash_flows)