def euclids_algorithm(q, r):
    remainder = q % r
    if remainder == 0:
        return r
    else:
        return euclids_algorithm(r, remainder)


def gcd(a, b):
    if a <= 0 or b <= 0:
        print(f"a and b must be greater than 0")
        exit(1)
    if a == 1 or b == 1:
        return 1
    if a > b:
        return euclids_algorithm(a, b)
    else:
        return euclids_algorithm(b, a)


if __name__ == "__main__":
    print(f"gcd(1160718174, 316258250) = {gcd(1160718174, 316258250)}")
    print(f"gcd(12345,67890) = {gcd(12345,67890)}")
    print(f"gcd(54321,9876) = {gcd(54321,9876)}")
