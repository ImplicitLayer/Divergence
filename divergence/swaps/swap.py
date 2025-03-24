# swap.py

class Swap:
    def __init__(self, notional, payment_frequency, maturity):
        """1
        Инициализация базового свопа.

        :param notional: Номинал свопа (основная сумма).
        :param payment_frequency: Частота платежей (например, 1 для ежегодных, 2 для полугодовых).
        :param maturity: Срок свопа в годах.
        """
        self.notional = notional
        self.payment_frequency = payment_frequency
        self.maturity = maturity

    def present_value(self, cash_flows, discount_rate):
        """
        Рассчитывает текущую стоимость денежных потоков.

        :param cash_flows: Список денежных потоков.
        :param discount_rate: Ставка дисконтирования.
        :return: Текущая стоимость денежных потоков.
        """
        pv = sum(cf / (1 + discount_rate) ** i for i, cf in enumerate(cash_flows, start=1))
        return pv


class InterestRateSwap(Swap):
    def __init__(self, notional, fixed_rate, payment_frequency, maturity):
        super().__init__(notional, payment_frequency, maturity)
        self.fixed_rate = fixed_rate

    def calculate_fixed_cash_flows(self):
        cash_flows = []
        for i in range(1, self.maturity * self.payment_frequency + 1):
            cash_flows.append(self.notional * self.fixed_rate / self.payment_frequency)
        return cash_flows

    def calculate_floating_cash_flows(self, floating_rates):
        cash_flows = []
        for rate in floating_rates:
            cash_flows.append(self.notional * rate / self.payment_frequency)
        return cash_flows

    def swap_value(self, floating_rates, discount_rate):
        fixed_cash_flows = self.calculate_fixed_cash_flows()
        floating_cash_flows = self.calculate_floating_cash_flows(floating_rates)

        pv_fixed = self.present_value(fixed_cash_flows, discount_rate)
        pv_floating = self.present_value(floating_cash_flows, discount_rate)

        return pv_floating - pv_fixed


class CurrencySwap(Swap):
    def __init__(self, notional_a, notional_b, fixed_rate_a, fixed_rate_b, payment_frequency, maturity):
        super().__init__(notional_a, payment_frequency, maturity)
        self.notional_a = notional_a
        self.notional_b = notional_b
        self.fixed_rate_a = fixed_rate_a
        self.fixed_rate_b = fixed_rate_b

    def calculate_fixed_cash_flows_a(self):
        cash_flows = []
        for i in range(1, self.maturity * self.payment_frequency + 1):
            cash_flows.append(self.notional_a * self.fixed_rate_a / self.payment_frequency)
        return cash_flows

    def calculate_fixed_cash_flows_b(self):
        cash_flows = []
        for i in range(1, self.maturity * self.payment_frequency + 1):
            cash_flows.append(self.notional_b * self.fixed_rate_b / self.payment_frequency)
        return cash_flows

    def swap_value(self, discount_rate):
        cash_flows_a = self.calculate_fixed_cash_flows_a()
        cash_flows_b = self.calculate_fixed_cash_flows_b()

        pv_a = self.present_value(cash_flows_a, discount_rate)
        pv_b = self.present_value(cash_flows_b, discount_rate)

        return pv_a - pv_b


class CommoditySwap(Swap):
    def __init__(self, notional, fixed_price, payment_frequency, maturity):
        super().__init__(notional, payment_frequency, maturity)
        self.fixed_price = fixed_price

    def calculate_fixed_cash_flows(self):
        cash_flows = []
        for i in range(1, self.maturity * self.payment_frequency + 1):
            cash_flows.append(self.notional * self.fixed_price / self.payment_frequency)
        return cash_flows

    def calculate_floating_cash_flows(self, floating_prices):
        cash_flows = []
        for price in floating_prices:
            cash_flows.append(self.notional * price / self.payment_frequency)
        return cash_flows

    def swap_value(self, floating_prices, discount_rate):
        fixed_cash_flows = self.calculate_fixed_cash_flows()
        floating_cash_flows = self.calculate_floating_cash_flows(floating_prices)

        pv_fixed = self.present_value(fixed_cash_flows, discount_rate)
        pv_floating = self.present_value(floating_cash_flows, discount_rate)

        return pv_floating - pv_fixed


# Пример использования
if __name__ == "__main__":
    # Пример процентного свопа
    notional = 1000000
    fixed_rate = 0.03
    payment_frequency = 2
    maturity = 5
    floating_rates = [0.025, 0.028, 0.032, 0.035, 0.03]
    discount_rate = 0.02

    ir_swap = InterestRateSwap(notional, fixed_rate, payment_frequency, maturity)
    ir_value = ir_swap.swap_value(floating_rates, discount_rate)
    print("Текущая стоимость процентного свопа:", ir_value)

    # Пример валютного свопа
    notional_a = 1000000
    notional_b = 800000
    fixed_rate_a = 0.03
    fixed_rate_b = 0.025
    currency_swap = CurrencySwap(notional_a, notional_b, fixed_rate_a, fixed_rate_b, payment_frequency, maturity)
    currency_value = currency_swap.swap_value(discount_rate)
    print("Текущая стоимость валютного свопа:", currency_value)

    # Пример товарного свопа
    commodity_notional = 1000
    fixed_price = 50
    floating_prices = [48, 52, 49, 51, 50]
    commodity_swap = CommoditySwap(commodity_notional, fixed_price, payment_frequency, maturity)
    commodity_value = commodity_swap.swap_value(floating_prices, discount_rate)
    print("Текущая стоимость товарного свопа:", commodity_value)