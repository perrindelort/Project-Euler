import math

from util.util import timing, format_number
from scripts.abstract_problem import Problem


class Problem53(Problem):
    def __init__(self, **kwargs):
        super().__init__()

        if "lower_bound" not in kwargs.keys():
            raise ValueError("lower_bound not specified")

        if "upper_bound" not in kwargs.keys():
            raise ValueError("upper_bound not specified")

        self.answer, self.time_taken = self.solve(
            lower_bound=kwargs["lower_bound"], upper_bound=kwargs["upper_bound"]
        )

        self.detailed_answer = f"The number of binomial coefficient for 1 ≤ n ≤ {format_number(kwargs['upper_bound'])} that are greater than {format_number(kwargs['lower_bound'])} is {format_number(self.answer)}"

    @timing
    def solve(self, lower_bound: int, upper_bound: int) -> int:
        count = 0
        # No particular optimisation but you can use binomial properties to evaluate only half of them I'd say
        for n in range(1, upper_bound + 1):
            for k in range(1, n):
                if math.comb(n, k) > lower_bound:
                    count += 1
        return count


if __name__ == "__main__":
    problem = Problem53(upper_bound=100, lower_bound=1_000_000)
    problem.print_problem()
