def left_to_right(x: list[int]) -> str:
    """Take a least significant first digit set and return a string representation of the number."""
    return "".join(str(d) for d in x[::-1])
    
def zero_pad(x: list[int], n: int, pad: int=0) -> list[int]:
    """Zero pad a list to the given length."""
    return [pad] * (n - len(x)) + x

def grade_school_multiplication(X: list[int], Y: list[int]) -> list[int]:
    # Pad the shorter list with zeros to match the lengths
    n = max(len(X), len(Y))
    X = zero_pad(X, n)
    Y = zero_pad(Y, n)

    # Initialize the result list W with zeros, length should be 2 * n
    W = [0] * (2 * n)

    # Multiply all partial products and add them to W
    for j in range(len(X)):
        for k in range(len(Y)):
            W[j + k] += X[j] * Y[k]

    # Handle carries from least significant to most significant digit
    for i in range(len(W) - 1):
        carry, W[i] = divmod(W[i], 10)
        W[i + 1] += carry

    # Remove excess leading zeros, if any, but leave at least one digit
    while len(W) > 1 and W[-1] == 0:
        W.pop()

    return W

def chunkify(x: list[int], h: int) -> list[int]:
    """Split a list into chunks of size n."""
    if len(x) % h != 0:
        raise ValueError(f"Length of list must be a multiple of {h}, {len(x)} is not!")
    n = len(x) // h
    chunks = [0]*n
    for ix, val in enumerate(x):
        chunks[ix // h] += val * 10**(ix % h)
    return chunks

def chunky_grade_school_multiplication(X: list[int], Y: list[int], h: int) -> list[int]:
    # Pad the shorter list with zeros to match the lengths
    n = max(len(X), len(Y))
    X = zero_pad(X, n)
    Y = zero_pad(Y, n)

    # Verify X and Y are chunkable
    if len(X) % h != 0:
        raise ValueError(f"Length of X must be a multiple of {h}, {len(X)} is not!")
    
    # Chunkify X and Y
    X = chunkify(X[:], h)
    Y = chunkify(Y[:], h)

    n = len(X_chunks)

    # Initialize the result list W with zeros, length should be 2 * n
    W = [0] * (2 * n)

    # Multiply all partial products and add them to W
    for j in range(len(X)):
        for k in range(len(Y)):
            W[j + k] += X[j] * Y[k]

    # Handle carries from least significant to most significant digit
    for i in range(len(W) - 1):
        carry, W[i] = divmod(W[i], 10**h)
        W[i + 1] += carry

    # Remove excess leading zeros, if any, but leave at least one digit
    while len(W) > 1 and W[-1] == 0:
        W.pop()

    return W


if __name__ == "__main__":
    # Grade School Multiplication
    X = [3,2,1]
    Y = [9,8,7]
    W = grade_school_multiplication(X, Y)

    print(f"X = {X} ({left_to_right(X)})")
    print(f"Y = {Y} ({left_to_right(Y)})")
    print(f"W = {W} ({left_to_right(W)})")

    # Chunky Grade School Multiplication
    X = [6,5,4,3,2,1]
    X_chunks = chunkify(X, 3)
    print(f"X = {X} ({left_to_right(X)})")
    print(f"X_chunks = {X_chunks} ({left_to_right(X_chunks)})")

    X = [6,5,4,3,2,1]
    Y = [4,5,6,7,8,9]
    W = chunky_grade_school_multiplication(X, Y, 3)

    print(f"X = {X} ({left_to_right(X)})")
    print(f"Y = {Y} ({left_to_right(Y)})")
    print(f"W = {W} ({left_to_right(W)})")
