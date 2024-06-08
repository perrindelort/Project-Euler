from typing import Tuple

from util.util import timing, format_number
from scripts.abstract_problem import Problem


class Problem71(Problem):
    def __init__(self, **kwargs):
        super().__init__()

        if "upper_bound" not in kwargs.keys():
            raise ValueError("upper_bound not specified")

        self.answer, self.time_taken = self.solve(upper_bound=kwargs["upper_bound"])

        self.detailed_answer = f"When listing the set of reduced proper fractions for d ≤ {format_number(kwargs['upper_bound'])}, the numerator of the fraction immediatly (which evaluates to  {format_number(self.answer[1])})to the left is {format_number(self.answer[0])}"

        # We returned 2 values for the detailed_answer
        self.answer = self.answer[0]

    @timing
    def solve(self, upper_bound: int) -> Tuple[int, int]:
        closest_numerator = 0
        closest = 2 / 5
        for d in range(2, upper_bound):
            for n in range(int(d * closest), d):
                val = n / d
                if val < 3 / 7:
                    if val > closest:
                        closest = val
                        closest_numerator = n
                else:
                    break
        return closest_numerator, closest


if __name__ == "__main__":
    problem = Problem71(upper_bound=1_000_000)
    problem.print_problem()
