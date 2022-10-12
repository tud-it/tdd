"""Contains utils."""

BEST_NUMBER: int = 42
NEED_NON_NEG_NUM: str = "Non-negative value expected."


def give_me_the_best_number() -> int:
    """Returns the best number."""

    return BEST_NUMBER


def fibonacci(count: int) -> tuple[int, ...]:
    """Computes Fibonacci sequence."""

    if count < 0:
        raise ValueError(NEED_NON_NEG_NUM)

    # if count < 3:
    #     return (1,) * count

    # nums = fibonacci(count - 1)
    # last = nums[-2] + nums[-1]

    # return nums + (last,)

    f0, f1, fn = 0, 1, 0
    numbers = []

    for __ in range(count):
        fn = f0 + f1
        f0 = f1
        f1 = fn

        numbers.append(f0)

    return tuple(numbers)
