def print_pyramid(n: int):
    # TODO: implement this function
    raise NotImplementedError


def print_inverted_pyramid(n: int):
    # TODO: implement this function
    for i in range(n, 0, -1):
        print(" " * (n - 1) + "*" * (2 * i - 1))


if __name__ == "__main__":
    N = int(input())
    print_pyramid(N)
    print_inverted_pyramid(N)
