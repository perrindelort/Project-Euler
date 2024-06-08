from util.util import timing, format_number
from scripts.abstract_problem import Problem


class Problem57(Problem):
    def __init__(self, **kwargs):
        super().__init__()

        if "upper_bound" not in kwargs.keys():
            raise ValueError("upper_bound not specified")

        self.answer, self.time_taken = self.solve(upper_bound=kwargs["upper_bound"])

        self.detailed_answer = f"In the first {format_number(kwargs['upper_bound'])} expansions there are {format_number(self.answer)} fractions which contain a numerator with more digits than the denominator"

    @timing
    def solve(self, upper_bound: int) -> int:
        count = 0
        numerator = 3
        denominator = 2
        for iteration in range(upper_bound - 1):
            numerator, denominator = (
                2 * denominator + numerator,
                denominator + numerator,
            )
            if len(str(numerator)) > len(str(denominator)):
                count += 1
        return count


if __name__ == "__main__":
    problem = Problem57(upper_bound=1_000)
    problem.print_problem()
