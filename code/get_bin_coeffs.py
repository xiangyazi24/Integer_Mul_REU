import math

def get_bin_coeffs(x):
    """Get binary coefficients for a large integer."""
    coeffs = []
    while x > 0:
        coeffs.append(x % 2)
        x >>= 1
    
    # Make sure coefficients are a power of two
    num_coeffs = len(coeffs)
    log2_len_coeffs = int(math.ceil(math.log(num_coeffs, 2)))
    len_coeffs = 2**log2_len_coeffs
    for _ in range(num_coeffs,len_coeffs):
        coeffs.append(0)
    return coeffs

get_bin_coeffs(10)
get_bin_coeffs(23353)