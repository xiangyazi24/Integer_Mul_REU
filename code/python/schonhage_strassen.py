from ntt import ntt, intt


def do_carries(w: list[int], h: int = 1) -> list[int]:
    for ix in range(len(w)-1):
        c, w[ix] = divmod(w[ix], 10**h)
        w[ix+1] += c
    return w


def print_num(num: list[int], var: str = 'w') -> None:
    print(f"{var} = {''.join([str(x) for x in num[::-1]]).lstrip('0')}")


def schonhage_strassen(x: list[int], y: list[int]) -> list[int]:
    """
    Perform simplified Schonhage-Strassen multiplication
    """
    print(f"{x=}")
    print(f"{y=}")
    n = len(x)
    # Primitive root of unity/generator for prime p
    w = 85
    # Prime for the finite field
    p = 337
    X = ntt(x, w, p)
    Y = ntt(y, w, p)
    print(f"{X=}")
    print(f"{Y=}")
    Z = [0] * n;
    for j in range(n):
        Z[j] = (X[j] * Y[j]) % p
    print(f"{Z=}")
    z = intt(Z, w, p)
    print(f"{z=}")
    return z


if __name__ == "__main__":
    x = [4,3,2,1,0,0,0,0]
    y = [9,8,7,6,0,0,0,0]
    z = schonhage_strassen(x, y)
    print(f"{z=}")
    z = do_carries(z, 1)
    print(f"{z=}")
    print_num(z, 'z')
