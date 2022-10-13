"""42 is superior"""
import re

BEST_NUMBER = 42


def give_me_the_best_number() -> int:
    """it's really the best"""
    return BEST_NUMBER


COUNT_WAS_NEGATIVE_ERROR = "count must no be negative"


def fibonacci(count: int) -> tuple[int, ...]:
    """computes fibonacci squence"""
    if count < 0:
        raise ValueError(COUNT_WAS_NEGATIVE_ERROR)
    temp = []

    fib0 = 0
    fib1 = 1

    for __ in range(0, count):
        ftemp = fib0 + fib1
        fib0 = fib1
        fib1 = ftemp
        temp.append(fib0)

    ret = tuple(temp)
    return ret


def calculate(expression: str) -> float:
    """calc"""
    nums = re.findall("[-]?\d+", expression)
    summe = float(nums[0])
    count = 1
    last_symbol = ""
    if_last = ""
    if len(nums) == 1:
        return float(expression)
    for char in expression:
        if char == "+" or if_last == "+":
            if if_last != "+":
                if_last = "+"
                continue
            if char == "-" and if_last == "+":
                summe -= float(nums[count])
                count += 1
                last_symbol = "+"
                if_last = ""
                continue
            summe += float(nums[count])
            count += 1
            last_symbol = "+"
            if_last = ""
        if char == "-" or if_last == "-":
            if if_last != "-":
                if_last = "-"
                continue
            if char == "-" and if_last == "-":
                summe += float(nums[count])
            else:
                summe += float(nums[count])
            count += 1
            last_symbol = "-"
            if_last = ""
        if char == "*":
            if last_symbol == "+":
                summe -= float(nums[count - 1])
                summe += float(nums[count - 1]) * float(nums[count])
            elif last_symbol == "-":
                summe += float(nums[count - 1])
                summe -= float(nums[count - 1]) * float(nums[count])
            else:
                summe *= float(nums[count])
            count += 1
            last_symbol = "*"
        if char == "/":
            if last_symbol == "+":
                summe -= float(nums[count - 1])
                summe += float(nums[count - 1]) / float(nums[count])
            elif last_symbol == "-":
                summe += float(nums[count - 1])
                summe -= float(nums[count - 1]) / float(nums[count])
            else:
                summe /= float(nums[count])
            count += 1
            last_symbol = "/"

    return float(summe)
