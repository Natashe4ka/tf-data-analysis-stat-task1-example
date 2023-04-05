import pandas as pd
import numpy as np


chat_id = 965404933 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    t = 88

    D = (sum([(x[i]-x.mean())**2 for i in range(x.shape[0])]))/(x.shape[0]-1)

    return D/t # Ваш ответ
