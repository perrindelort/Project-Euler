from functools import cache
from typing import Tuple

from util.util import timing, format_number
from scripts.abstract_problem import Problem


@cache
def collatz_sequence(n):
    if n == 2:
        return 1
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


class Problem14(Problem):
    def __init__(self, **kwargs):
        super().__init__()

        if "upper_bound" not in kwargs.keys():
            raise ValueError("upper_bound not specified")

        self.answer, self.time_taken = self.solve(upper_bound=kwargs["upper_bound"])

        self.detailed_answer = f"The starting number under {format_number(kwargs['upper_bound'])} producing the longest chain is {format_number(self.answer[0])} with a {format_number(self.answer[1])}-long chain"

        # Because we returned 2 arguments for the detailed_answer
        self.answer = self.answer[0]

    @timing
    def solve(self, upper_bound: int) -> Tuple[int, int]:
        # May still be improved by keeping tracks of all collatz lengths and if n < i then adding the corresponding lengths
        max_length = 0
        start = 0
        for i in range(1, upper_bound + 1):
            length = 1
            n = i
            while n != 1:
                n = collatz_sequence(n)
                length += 1
            if length > max_length:
                max_length = length
                start = i
        return (start, max_length)


if __name__ == "__main__":
    problem = Problem14(upper_bound=1_000_000)
    problem.print_problem()
