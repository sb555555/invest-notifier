import pandas as pd
import numpy as np
import yfinance as yf
from pyxirr import xirr
from datetime import datetime, timedelta


LARGECAP = "^NSEI"
MIDCAP = ""
SMALLCAP = ""
MICROCAP = ""
BUY_ATFER = 1

funds = [LARGECAP, MIDCAP, SMALLCAP, MICROCAP]
RSI_THRESHOLDS = [10, 10, 10, 10]


def calculate_RSI(data, window=14):

    delta = data['Close'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    return rsi

def main():
    today = datetime.today()
    start = today - timedelta(days=20)

    START = str(start.date())
    END = str(today.date())

    result = []

    for fund, rsi_threshold in zip(funds[:1], RSI_THRESHOLDS):

        data = yf.download(fund, START, END, progress=False)
        rsi = calculate_RSI(data, window=2)
        result.append((fund, rsi[-1], rsi_threshold, "NO BUY"))
    
    return result
