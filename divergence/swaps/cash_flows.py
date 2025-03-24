class CashFlow:
    def __init__(self, amount, time_period):
        """
        Инициализация денежного потока.

        :param amount: Сумма денежного потока.
        :param time_period: Период времени, когда происходит денежный поток (в годах).
        """
        self.amount = amount
        self.time_period = time_period

    def present_value(self, discount_rate):
        """
        Рассчитывает текущую стоимость денежного потока.

        :param discount_rate: Ставка дисконтирования.
        :return: Текущая стоимость денежного потока.
        """
        return self.amount / (1 + discount_rate) ** self.time_period


class CashFlowSeries:
    def __init__(self):
        """Инициализация серии денежных потоков."""
        self.cash_flows = []

    def add_cash_flow(self, cash_flow):
        """
        Добавляет денежный поток в серию.

        :param cash_flow: Объект CashFlow.
        """
        self.cash_flows.append(cash_flow)

    def total_present_value(self, discount_rate):
        """
        Рассчитывает общую текущую стоимость всех денежных потоков в серии.

        :param discount_rate: Ставка дисконтирования.
        :return: Общая текущая стоимость.
        """
        total_pv = sum(cf.present_value(discount_rate) for cf in self.cash_flows)
        return total_pv

    def __str__(self):
        """Возвращает строковое представление серии денежных потоков."""
        return "\n".join(f"Cash Flow: {cf.amount} at time {cf.time_period}" for cf in self.cash_flows)


# Пример использования
if __name__ == "__main__":
    # Создание серии денежных потоков
    cash_flow_series = CashFlowSeries()

    # Добавление денежных потоков
    cash_flow_series.add_cash_flow(CashFlow(1000, 1))
    cash_flow_series.add_cash_flow(CashFlow(1500, 2))
    cash_flow_series.add_cash_flow(CashFlow(2000, 3))

    # Вывод информации о серии денежных потоков
    print("Серия денежных потоков:")
    print(cash_flow_series)

    # Расчет общей текущей стоимости
    discount_rate = 0.05
    total_pv = cash_flow_series.total_present_value(discount_rate)
    print(f"\nОбщая текущая стоимость при ставке дисконтирования {discount_rate * 100}%: {total_pv:.2f}")
