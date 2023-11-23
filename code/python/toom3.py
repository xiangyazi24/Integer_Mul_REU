import numpy as np


def pad(x: str, h: int) -> str:
    r = len(x) % h
    if r != 0:
        padding = ['0'] * (h - r)
        return "".join(padding) + x
    return x


def chunkify(x: str, h: int) -> list[int]:
    if len(x) % h != 0:
        print(f"Length of {x} is not an integer multiple of {h}, exiting")
        exit(1)
    return [int(x[max(i - 8, 0):i]) for i in range(len(x), 0, -8)]


def print_coeffs(chunks: list[int], coeff: str = 'x') -> None:
    for ix, chunk in enumerate(chunks):
        print(f"{coeff}_{ix} = {chunk}")


def eval_input_poly(x: list[int]) -> list[int]:
    """x is the coefficients, returns a list of values at our chosen Toom-3 points.
    The points are {0, 1, -1, -2, \infty}"""
    gamma = x[0] + x[2]
    x_of_zero = x[0]
    x_of_one = gamma + x[1]
    x_of_minus_one = gamma - x[1]
    x_of_minus_two = 2*(x_of_minus_one + x[2]) - x[0]
    x_of_infty = x[2]
    x_of_t = [x_of_zero, x_of_one, x_of_minus_one, x_of_minus_two, x_of_infty]
    return x_of_t


def multiply_points(x: list[int], y: list[int]) -> list[int]:
    w = [0] * len(x)
    for ix in range(len(x)):
        w[ix] = x[ix]*y[ix]
    return w


def print_points(x: list[int], var: 'str') -> None:
    print(f"{var}(0)   = {x[0]}")
    print(f"{var}(1)   = {x[1]}")
    print(f"{var}(-1)  = {x[2]}")
    print(f"{var}(-2)  = {x[3]}")
    print(f"{var}(inf) = {x[4]}")


def interp_w(p: list[int]) -> list[int]:
    """p is the list of points for w"""
    w = [0] * 5
    w[0] = p[0]
    w[1] = (1/2)*p[0] + (1/3)*p[1] - p[2] + (1/6)*p[3] - 2*p[4]
    w[2] = -p[0] + (1/2)*p[1] + (1/2)*p[2] - p[4]
    w[3] = -(1/2)*p[0] + (1/6)*p[1] + (1/2)*p[2] - (1/6)*p[3] + 2*p[4]
    w[4] = p[4]
    for ix in range(len(w)):
        w[ix] = int(w[ix])
    return w

def do_carries(w: list[int], h: int = 1) -> list[int]:
    for ix in range(len(w)-1):
        c, w[ix] = divmod(w[ix], 10**h)
        w[ix+1] += c
    return w


def print_num(num: list[int], var: str = 'w') -> None:
    print(f"{var} = {''.join([str(x) for x in num[::-1]])}")


if __name__ == "__main__":
    h = 8

    x = "698310488572646777019184"
    y = "144585992498882884065634"
    x = pad(x, h)
    y = pad(y, h)
    print(f"x = {x}")
    x_chunks = chunkify(x, h)
    print_coeffs(x_chunks, 'x')
    print(f"y = {y}")
    y_chunks = chunkify(y, h)
    print_coeffs(y_chunks, 'y')

    x_of_t = eval_input_poly(x_chunks)
    y_of_t = eval_input_poly(y_chunks)
    print_points(x_of_t, 'x')
    print_points(y_of_t, 'y')

    w_of_t = multiply_points(x_of_t, y_of_t)
    print_points(w_of_t, 'w')

    w = interp_w(w_of_t)
    print_coeffs(w, 'w')

    do_carries(w, h)
    print_num(w)
