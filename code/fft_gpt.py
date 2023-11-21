import cmath

def fft(a):
    n = len(a)
    if n == 1:
        return a
    w_n = cmath.exp(2j * cmath.pi / n)
    w = 1
    a0 = a[::2]
    a1 = a[1::2]
    y0 = fft(a0)
    y1 = fft(a1)
    y = [0] * n
    for k in range(n // 2):
        y[k] = y0[k] + w * y1[k]
        y[k + n // 2] = y0[k] - w * y1[k]
        w *= w_n
    return y

def ifft(a):
    n = len(a)
    a_conjugate = [x.conjugate() for x in a]
    y = fft(a_conjugate)
    return [x.conjugate() / n for x in y]

def pad_with_zeros(a, b):
    n = 1
    while n < len(a) + len(b):
        n *= 2
    return a + [0] * (n - len(a)), b + [0] * (n - len(b))

def large_int_multiplication(a, b):
    a = [int(digit) for digit in a][::-1]
    b = [int(digit) for digit in b][::-1]
    a, b = pad_with_zeros(a, b)
    fft_a = fft(a)
    fft_b = fft(b)
    fft_product = [x * y for x, y in zip(fft_a, fft_b)]
    product_poly = ifft(fft_product)
    product = [round(x.real) for x in product_poly]  # Round to correct floating point errors
    carry = 0
    for i in range(len(product)):
        product[i] += carry
        carry = product[i] // 10
        product[i] %= 10
    while len(product) > 1 and product[-1] == 0:
        product.pop()  # Remove trailing zeros
    return int(''.join(map(str, product[::-1])))

# Example usage
print(large_int_multiplication("123456789", "987654321"))
