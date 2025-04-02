from divergence.swaps.cash_flows import *
from divergence.swaps.swap import *
from divergence.swaps.valuation import *

# Cash flow
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

# Swap
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

# valuation
# Оценка процентного свопа
swap = InterestRateSwapValuation(notional=1000000, fixed_rate=0.03, floating_rate=0.025, payment_frequency=2, years_to_maturity=5)
market_rate = 0.02
npv = swap.net_present_value(market_rate)
print(f"Чистая текущая стоимость процентного свопа: {npv:.2f}")

# Оценка валютного свопа
currency_swap = CurrencySwapValuation(notional_a=1000000, notional_b=800000, fixed_rate_a=0.02, fixed_rate_b=0.025, payment_frequency=2, years_to_maturity=5)
market_rate_a = 0.015
market_rate_b = 0.02
npv_currency = currency_swap.net_present_value(market_rate_a, market_rate_b)
print(f"Чистая текущая стоимость валютного свопа: {npv_currency:.2f}")

# Оценка товарного свопа
commodity_swap = CommoditySwapValuation(notional=1000, fixed_price=50, floating_price=55, payment_frequency=2, years_to_maturity=5)
market_price = 52
npv_commodity = commodity_swap.net_present_value(market_price)
print(f"Чистая текущая стоимость товарного свопа: {npv_commodity:.2f}")
