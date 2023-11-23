def ntt(x: list[int], w: int, p: int) -> list[int]:
    """
    Returns the number-theoretic transform of x with p where w is the generator/root of unity
    """
    n = len(x)
    if n == 1:
        return x
    else:
        x_even = ntt(x[0::2], pow(w, 2, p), p)
        x_odd = ntt(x[1::2], pow(w, 2, p), p)
        combined = [0] * n
        y = 1
        for j in range(n // 2):
            combined[j] = (x_even[j] + y * x_odd[j]) % p
            combined[j + n // 2] = (x_even[j] - y * x_odd[j]) % p
            y = (y * w) % p
        return combined

def intt(X: list[int], w: int, p: int) -> list[int]:
    inv_w = modinv(w, p)
    n = len(X)
    inv_n = modinv(n, p)
    x = ntt(X, inv_w, p)
    x_norm = [val * inv_n % p for val in x]
    return x_norm


def modinv(a: int, p: int) -> int:
    return pow(a, p-2, p)


if __name__ == "__main__":
    x1 = [4,3,2,1,0,0,0,0]
    x2 = [8,7,6,5,0,0,0,0]
    w = 85
    p = 337
    print(f"{x1=}")
    print(f"{x2=}")
    X1 = ntt(x1, w, p)
    X2 = ntt(x2, w, p)
    print(f"{X1=}")
    print(f"{X2=}")
    x1_prime = intt(X1, w, p)
    x2_prime = intt(X2, w, p)
    print(f"{x1_prime=}")
    print(f"{x2_prime=}")
    