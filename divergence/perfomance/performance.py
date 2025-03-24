import numpy as np
import pandas as pd


class PerformanceAnalyzer:
    def __init__(self, returns, benchmark_returns=None):
        self.returns = pd.Series(returns)
        self.benchmark_returns = pd.Series(benchmark_returns) if benchmark_returns is not None else None

    def calculate_cumulative_return(self):
        return (1 + self.returns).cumprod() - 1

    def calculate_annualized_return(self):
        total_return = self.calculate_cumulative_return().iloc[-1]
        n_years = len(self.returns) / 252
        return (1 + total_return) ** (1 / n_years) - 1

    def calculate_volatility(self):
        return self.returns.std() * np.sqrt(252)

    def calculate_sharpe_ratio(self, risk_free_rate=0.0):
        excess_returns = self.returns - risk_free_rate / 252
        return excess_returns.mean() / excess_returns.std() * np.sqrt(252)

    def calculate_sortino_ratio(self, target_return=0.0):
        downside_returns = self.returns[self.returns < target_return]
        downside_deviation = downside_returns.std() * np.sqrt(252)
        excess_returns = self.returns.mean() - target_return / 252
        return excess_returns / downside_deviation if downside_deviation != 0 else np.nan

    def calculate_max_drawdown(self):
        cumulative_returns = self.calculate_cumulative_return()
        peak = cumulative_returns.cummax()
        drawdown = (cumulative_returns - peak) / peak
        return drawdown.min()

    def calculate_average_drawdown(self):
        cumulative_returns = self.calculate_cumulative_return()
        peak = cumulative_returns.cummax()
        drawdowns = (cumulative_returns - peak) / peak
        return drawdowns[drawdowns < 0].mean()

    def calculate_information_ratio(self):
        if self.benchmark_returns is None:
            raise ValueError("Benchmark returns must be provided to calculate Information Ratio.")
        excess_returns = self.returns - self.benchmark_returns
        return excess_returns.mean() / excess_returns.std() * np.sqrt(252)

    def calculate_alpha(self, risk_free_rate=0.0):
        if self.benchmark_returns is None:
            raise ValueError("Benchmark returns must be provided to calculate Alpha.")
        benchmark_annualized_return = (1 + self.benchmark_returns).cumprod().iloc[-1] ** (252 / len(self.benchmark_returns)) - 1
        return self.calculate_annualized_return() - (risk_free_rate + benchmark_annualized_return)

    def calculate_beta(self):
        if self.benchmark_returns is None:
            raise ValueError("Benchmark returns must be provided to calculate Beta.")
        covariance = np.cov(self.returns, self.benchmark_returns)[0][1]
        benchmark_variance = self.benchmark_returns.var()
        return covariance / benchmark_variance

    def summary(self):
        print("Кумулятивная доходность:", self.calculate_cumulative_return().iloc[-1])
        print("Годовая доходность:", self.calculate_annualized_return())
        print("Волатильность:", self.calculate_volatility())
        print("Коэффициент Шарпа:", self.calculate_sharpe_ratio())
        print("Коэффициент Сортино:", self.calculate_sortino_ratio())
        print("Максимальная просадка:", self.calculate_max_drawdown())
        print("Средняя просадка:", self.calculate_average_drawdown())
        if self.benchmark_returns is not None:
            print("Коэффициент информации:", self.calculate_information_ratio())
            print("Альфа:", self.calculate_alpha())
            print("Бета:", self.calculate_beta())


if __name__ == "__main__":
    np.random.seed(42)
    returns = pd.Series(np.random.normal(0.001, 0.02, 252))  # 252 торговых дня
    benchmark_returns = pd.Series(np.random.normal(0.0005, 0.015, 252))  # Бенчмарк

    analyzer = PerformanceAnalyzer(returns, benchmark_returns)
    analyzer.summary()