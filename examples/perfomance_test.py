from divergence.perfomance.performance import PerformanceAnalyzer
import numpy as np
import pandas as pd

np.random.seed(42)
returns = pd.Series(np.random.normal(0.001, 0.02, 252))  # 252 торговых дня
benchmark_returns = pd.Series(np.random.normal(0.0005, 0.015, 252))  # Бенчмарк

analyzer = PerformanceAnalyzer(returns, benchmark_returns)
analyzer.summary()
