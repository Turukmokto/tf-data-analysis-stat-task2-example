import pandas as pd
import numpy as np

from scipy.stats import gamma

chat_id = 1112700607  # Ваш chat ID, не меняйте название переменной

def ans(a, l, n):
    return (l + gamma.ppf(a / 2, n) / n - 1 / 2) * 2 / 50 ** 2

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    l = x.mean()
    n = x.size
    return ans(1 + p, l, n), ans(1 - p, l, n)
