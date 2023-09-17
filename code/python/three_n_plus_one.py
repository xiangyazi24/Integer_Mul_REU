def three_n_plus_one(n, num=0):
    if n == 1:
        print(f"{n}")
        print(f"Called {num+1} times")
        return ""
    else:
        print(f"{n}, ", end="")
        if n % 2 == 0:
            return three_n_plus_one(n//2, num+1)
        else:
            return three_n_plus_one(3*n+1, num+1)


if __name__ == "__main__":
    print(f"{three_n_plus_one(5)}")
    print(f"{three_n_plus_one(7)}")
    print(f"{three_n_plus_one(21)}")
    print(f"{three_n_plus_one(13)}")
    print(f"{three_n_plus_one(31)}")

