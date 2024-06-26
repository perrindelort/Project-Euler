import numpy as np

from collections import Counter
from primePy import primes

from util.util import timing, format_number
from scripts.abstract_problem import Problem


class Problem47(Problem):
    def __init__(self, **kwargs):
        super().__init__()

        if "upper_bound" not in kwargs.keys():
            raise ValueError("upper_bound not specified")

        self.answer, self.time_taken = self.solve(upper_bound=kwargs["upper_bound"])

        self.detailed_answer = f"The first of the first four consecutive integers to have four distinct prime factors each is {format_number(self.answer)}"

    @timing
    def solve(self, upper_bound: int) -> int:
        supremum = 1000000
        integer = np.prod(primes.first(4)) - 1
        while integer <= upper_bound:
            in_a_row = 0
            integer += 1
            is_true = len(Counter(primes.factors(integer))) == 4
            while is_true:
                in_a_row += 1
                if in_a_row == 4:
                    return integer - 4 + 1
                if is_true:
                    integer += 1
                    is_true = len(Counter(primes.factors(integer))) == 4
        else:
            self.solve(upper_bound * 100)


if __name__ == "__main__":
    problem = Problem47(upper_bound=1_000_000)
    problem.print_problem()
