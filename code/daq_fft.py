import numpy as np 


#Source: https://jakevdp.github.io/blog/2013/08/28/understanding-the-fft/
def daq_fft(x):
    """A divide and conquer, recursive implementation of the 1D Cooley-Tukey FFT"""
    x = np.asarray(x, dtype=float)
    N = x.shape[0]

    if N % 2 > 0:
        raise ValueError("size of x must be a power of 2")
    elif N <= 32:  # this cutoff should be optimized
        return dft_slow(x)
    else:
        X_even = daq_fft(x[::2])
        X_odd = daq_fft(x[1::2])
        factor = np.exp(-2j * np.pi * np.arange(N) / N)
        return np.concatenate([X_even + factor[:N / 2] * X_odd,
                               X_even + factor[N / 2:] * X_odd])
    