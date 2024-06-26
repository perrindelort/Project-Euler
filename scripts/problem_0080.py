from sympy import N, sqrt

from util.util import timing, format_number
from scripts.abstract_problem import Problem


class Problem80(Problem):
    def __init__(self, **kwargs):
        super().__init__()

        if "upper_bound" not in kwargs.keys():
            raise ValueError("upper_bound not specified")

        self.answer, self.time_taken = self.solve(upper_bound=kwargs["upper_bound"])

        self.detailed_answer = f"The total of the digital sums of the first one hundred decimal digits for all the irrational square roots is {format_number(self.answer)}"

    @timing
    def solve(self, upper_bound: int) -> int:
        s = 0
        rationals = [i**2 for i in range(10)]
        for integer in range(2, upper_bound):
            if integer not in rationals:
                digits = str(N(sqrt(integer), 150))[:101]
                for digit in digits:
                    if digit != ".":
                        s += int(digit)
        return s


if __name__ == "__main__":
    problem = Problem80(upper_bound=100)
    problem.print_problem()
