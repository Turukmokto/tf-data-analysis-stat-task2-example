import pandas as pd
import numpy as np

from scipy.stats import gamma

chat_id = 1112700607  # Ваш chat ID, не меняйте название переменной

def ans(val, sm, n):
    return ((sm + gamma.ppf(val, a=n)) / n - 1) * 2 / 50 ** 2

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    al = 1 - p
    sm = (x + 1 / 2).sum()
    n = len(x)
    return ans(al / 2, sm, n), ans(1 - al / 2, sm, n)
