import pandas as pd
import numpy as np

from scipy.stats import norm

chat_id = 1112700607  # Ваш chat ID, не меняйте название переменной


def ans(power, l, shift):
    return (l - shift * norm.ppf(power)) * 2 / 50 ** 2


def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    a = 1 - p
    l = x.mean()
    shift = np.sqrt(np.var(x)) / np.sqrt(len(x))
    return ans(1 - a / 2, l, shift), ans(a / 2, l, shift)

