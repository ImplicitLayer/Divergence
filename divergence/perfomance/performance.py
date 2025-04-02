import numpy as np
import pandas as pd


class PerformanceAnalyzer:
    """
    A class to analyze the performance of investment returns.

    :param returns: A list or array-like object containing the returns of the investment.
    :param benchmark_returns: (Optional) A list or array-like object containing the benchmark returns.
    """

    def __init__(self, returns, benchmark_returns=None):
        """
        Initializes the PerformanceAnalyzer with investment and optional benchmark returns.

        :param returns: A list or array-like object containing the returns of the investment.
        :param benchmark_returns: (Optional) A list or array-like object containing the benchmark returns.
        """
        self.returns = pd.Series(returns)
        self.benchmark_returns = pd.Series(benchmark_returns) if benchmark_returns is not None else None

    def calculate_cumulative_return(self):
        """
        Calculate cumulative return of the investment.

        :return: Cumulative return as a float.
        """
        return (1 + self.returns).cumprod() - 1

    def calculate_annualized_return(self):
        """
        Calculate annualized return of the investment.

        :return: Annualized return as a float.
        """
        total_return = self.calculate_cumulative_return().iloc[-1]
        n_years = len(self.returns) / 252
        return (1 + total_return) ** (1 / n_years) - 1

    def calculate_volatility(self):
        """
        Calculate annualized volatility of the investment.

        :return: Annualized volatility as a float.
        """
        return self.returns.std() * np.sqrt(252)

    def calculate_sharpe_ratio(self, risk_free_rate=0.0):
        """
        Calculate Sharpe Ratio of the investment.

        :param risk_free_rate: Risk-free rate as a float (default is 0.0).

        :return: Sharpe Ratio as a float.
        """
        excess_returns = self.returns - risk_free_rate / 252
        return excess_returns.mean() / excess_returns.std() * np.sqrt(252)

    def calculate_sortino_ratio(self, target_return=0.0):
        """
        Calculate Sortino Ratio of the investment.

        :param target_return: Target return to compare against (default is 0.0).

        :return: Sortino Ratio as a float.
        """
        downside_returns = self.returns[self.returns < target_return]
        downside_deviation = downside_returns.std() * np.sqrt(252)
        excess_returns = self.returns.mean() - target_return / 252
        return excess_returns / downside_deviation if downside_deviation != 0 else np.nan

    def calculate_max_drawdown(self):
        """
        Calculate maximum drawdown of the investment.

        :return: Maximum drawdown as a float.
        """
        cumulative_returns = self.calculate_cumulative_return()
        peak = cumulative_returns.cummax()
        drawdown = (cumulative_returns - peak) / peak
        return drawdown.min()

    def calculate_average_drawdown(self):
        """
        Calculate average drawdown of the investment.

        :return: Average drawdown as a float.
        """
        cumulative_returns = self.calculate_cumulative_return()
        peak = cumulative_returns.cummax()
        drawdowns = (cumulative_returns - peak) / peak
        return drawdowns[drawdowns < 0].mean()

    def calculate_information_ratio(self):
        """
        Calculate Information Ratio of the investment compared to its benchmark.

        :raises ValueError: If benchmark returns are not provided.

        :return: Information Ratio as a float.
        """
        if self.benchmark_returns is None:
            raise ValueError("Benchmark returns must be provided to calculate Information Ratio.")
        excess_returns = self.returns - self.benchmark_returns
        return excess_returns.mean() / excess_returns.std() * np.sqrt(252)

    def calculate_alpha(self, risk_free_rate=0.0):
        """
        Calculate Alpha of the investment compared to its benchmark.

        :param risk_free_rate: Risk-free rate as a float (default is 0.0).

        :raises ValueError: If benchmark returns are not provided.

        :return: Alpha as a float.
        """
        if self.benchmark_returns is None:
            raise ValueError("Benchmark returns must be provided to calculate Alpha.")
        benchmark_annualized_return = (1 + self.benchmark_returns).cumprod().iloc[-1] ** (
                    252 / len(self.benchmark_returns)) - 1
        return self.calculate_annualized_return() - (risk_free_rate + benchmark_annualized_return)

    def calculate_beta(self):
        """
        Calculate Beta of the investment compared to its benchmark.

        :raises ValueError: If benchmark returns are not provided.

        :return: Beta as a float.
        """
        if self.benchmark_returns is None:
            raise ValueError("Benchmark returns must be provided to calculate Beta.")
        covariance = np.cov(self.returns, self.benchmark_returns)[0][1]
        benchmark_variance = self.benchmark_returns.var()
        return covariance / benchmark_variance

    def summary(self):
        """
        Print a summary of performance metrics including cumulative return,
        annualized return, volatility, Sharpe ratio, Sortino ratio,
        maximum drawdown, average drawdown, and information ratio,
        alpha and beta if benchmark returns are provided.
        """
        print("Cumulative Return:", self.calculate_cumulative_return().iloc[-1])
        print("Annualized Return:", self.calculate_annualized_return())
        print("Volatility:", self.calculate_volatility())
        print("Sharpe Ratio:", self.calculate_sharpe_ratio())
        print("Sortino Ratio:", self.calculate_sortino_ratio())
        print("Maximum Drawdown:", self.calculate_max_drawdown())
        print("Average Drawdown:", self.calculate_average_drawdown())
        if self.benchmark_returns is not None:
            print("Information Ratio:", self.calculate_information_ratio())
            print("Alpha:", self.calculate_alpha())
            print("Beta:", self.calculate_beta())
