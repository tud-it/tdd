"""Contains functionality to calculate a float value from a string expression."""

from enum import Enum


class Operator(Enum):
    """Specifies different mathematical operations."""

    ADD = 0
    SUB = 1
    MUL = 2
    DIV = 3


# Maps the string representations of the operators to the enum.
ops_map: dict[str, Operator] = {
    "+": Operator.ADD,
    "-": Operator.SUB,
    "*": Operator.MUL,
    "/": Operator.DIV,
}


class Expr:
    """Parses and evaluates a given string expression."""

    # Double-underscored class variables become "private" to the class.
    __expr: str
    __length: int

    __position: int
    __operands: list  # Can contain numbers, or other Expr (parentheses).
    __operations: list[Operator]

    def __init__(self, expression: str) -> None:
        self.__expr = expression
        self.__length = len(expression)

        self.__position = 0
        self.__operands = []
        self.__operations = []

    def __parse(self) -> int:
        curr: str = ""

        while self.__position < self.__length:
            char: str = self.__expr[self.__position]

            if char == "(":  # Opening parenthesis just begun.
                curr = self.__expr[self.__position + 1 :]

                # Create expression from everything inside of the parens.
                expr = Expr(curr)

                self.__position += expr.__parse()  # Skip until closing parens.
                self.__operands.append(expr)

                curr = ""

            if char in ops_map:
                if curr:  # curr != ""
                    self.__operands.append(float(curr))
                    curr = ""

                self.__operations.append(ops_map[char])

            if char.isdigit():
                curr += char  # Build current number one by one.

            self.__position += 1

            if char == ")":  # Closing parens of current expr.
                break

        self.__operands.append(float(curr))

        return self.__position  # Amount of positions advanced in expr.

    def evaluate(self) -> float:
        """Evaluates the given expression and returns the result."""

        _ = self.__parse()

        return 0
