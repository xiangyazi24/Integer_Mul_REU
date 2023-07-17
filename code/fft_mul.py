import numpy as np

def fft_mul(a, b):
    # Convert the numbers to strings to work with individual digits
    a = str(a)
    b = str(b)
    
    # Determine the size for FFT: it must be a power of 2 and greater than the sum of input sizes
    n = 1
    while n < len(a) + len(b): 
        n *= 2
    
    # Convert the numbers to arrays of digits, padded with zeros
    a = np.array([int(d) for d in a[::-1]] + [0]*(n-len(a)), dtype=int)
    b = np.array([int(d) for d in b[::-1]] + [0]*(n-len(b)), dtype=int)
    
    # Perform FFT
    fft_a = np.fft.fft(a)
    fft_b = np.fft.fft(b)
    
    # Multiply in the frequency domain
    fft_c = fft_a * fft_b
    
    # Convert back to the time domain
    c = np.fft.ifft(fft_c).real.round().astype(int)
    
    # Carry over the digits
    for i in range(len(c)-1):
        c[i+1] += c[i] // 10
        c[i] %= 10
    
    # Convert back to integer (as a string to prevent overflow)
    result = ''.join(str(x) for x in c[::-1]).lstrip('0')  # reverse, convert to string, remove leading zeros
    
    return int(result)  # convert to integer for final output, if necessary
