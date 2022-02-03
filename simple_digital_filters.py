import numpy as np


def factorize(x, k):
    return x * k


def left_shift(x, offset=1):
    if offset == 0:
        return x
    if offset < 0 or offset > x.size:
        raise Exception("invalid offset !")
    return [x[i + offset] if i + offset <= x.size - 1 else np.nan for i in range(x.size)]
    '''
    y = [np.nan] * x.size
    for i in range(x.size):
        if i + offset <= x.size - 1:
            y[i] = x[i + offset]
    return y
    '''


def right_shift(x, offset=1):
    if offset == 0:
        return x
    if offset < 0 or offset > x.size:
        raise Exception("invalid offset !")
    return [x[i - offset] if i >= offset else np.nan for i in range(x.size)]
    '''
    y = [np.nan] * x.size
    for i in range(x.size):
        if i >= offset:
            y[i] = x[i - offset]
    return y
    '''


def shift(x, offset=1):
    return right_shift(x, offset) if offset >= 0 else left_shift(x, abs(offset))


def diff(x):
    return [x[i] - x[i - 1] if not i == 0 else np.nan for i in range(x.size)]
    '''
    y = [np.nan] * x.size
    for i in range(1, x.size):
        y[i] = x[i] - x[i-1]
    return y
    '''


def reverse(x):
    y = [np.nan] * x.size
    y[0] = 0.5 * x[0]
    y[1] = y[0] + 0.5 * x[1]
    for i in range(2, x.size):
        y[i] = y[i - 1] + 0.5 * (x[i] - x[i - 2])
    return y


def smooth(x, window_len=11, window='hanning'):

    if x.ndim != 1:
        raise ValueError ("smooth only accepts 1 dimension arrays.")

    if x.size < window_len:
        raise ValueError ("Input vector needs to be bigger than window size.")

    if window_len < 3:
        return x

    if not window in ['flat', 'hanning', 'hamming', 'bartlett', 'blackman']:
        raise ValueError ("Window is on of 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'")

    s = np.r_[x[window_len - 1:0:-1], x, x[-2:-window_len - 1:-1]]
    # print(len(s))
    if window == 'flat':  # moving average
        w = np.ones(window_len, 'd')
    else:
        w = eval('np.' + window + '(window_len)')

    y = np.convolve(w / w.sum(), s, mode='valid')
    return y

