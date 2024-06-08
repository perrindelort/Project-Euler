import scipy.special

from util.util import timing, format_number
from scripts.abstract_problem import Problem


class Problem15(Problem):
    def __init__(self, **kwargs):
        super().__init__()

        if "length" not in kwargs.keys():
            raise ValueError("length not specified")
        if "width" not in kwargs.keys():
            raise ValueError("width not specified")

        self.answer, self.time_taken = self.solve(
            length=kwargs["length"], width=kwargs["width"]
        )

        self.detailed_answer = f"In a {format_number(kwargs['length'])}x{format_number(kwargs['width'])} grid there are {format_number(self.answer)} such routes \nNOTE : There is no need for calculation as the problem is solvable on paper"

    @timing
    def solve(self, length: int, width: int) -> int:
        # We specify int here as the scipy function uses gamma function and thus return a float and not an int
        return int(scipy.special.binom(length + width, width))


if __name__ == "__main__":
    problem = Problem15(length=20, width=20)
    problem.print_problem()
