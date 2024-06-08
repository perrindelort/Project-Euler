from util.util import timing, format_number
from scripts.abstract_problem import Problem


class Problem48(Problem):
    def __init__(self, **kwargs):
        super().__init__()

        if "upper_bound" not in kwargs.keys():
            raise ValueError("upper_bound not specified")

        self.answer, self.time_taken = self.solve(upper_bound=kwargs["upper_bound"])

        self.detailed_answer = f"The last 10 digits of the serie 1^1 + 2^2 + 3^3 + ... + {format_number(kwargs['upper_bound'])}^{format_number(kwargs['upper_bound'])} is {format_number(self.answer)}"

    @timing
    def solve(self, upper_bound: int) -> int:
        s = 0
        for i in range(1, upper_bound + 1):
            s += i**i
        sum_string = str(s)
        return int(sum_string[len(sum_string) - 10 :])


if __name__ == "__main__":
    problem = Problem48(upper_bound=1_000)
    problem.print_problem()
