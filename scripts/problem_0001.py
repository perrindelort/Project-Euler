from util.util import timing, format_number
from scripts.abstract_problem import Problem


class Problem1(Problem):
    def __init__(self, **kwargs):
        super().__init__()

        if "upper_bound" not in kwargs.keys():
            raise ValueError("upper_bound not specified")
        self.answer, self.time_taken = self.solve(upper_bound=kwargs["upper_bound"])

        self.detailed_answer = f"The sum of all the multiples of 3 or 5 below {format_number(kwargs['upper_bound'])} is {format_number(self.answer)}"

    @timing
    def solve(self, upper_bound: int) -> int:
        s = 0
        for n in range(upper_bound):
            if n % 3 == 0 or n % 5 == 0:
                s += n
        return s


if __name__ == "__main__":
    problem = Problem1(upper_bound=1_000)
    problem.print_problem()
