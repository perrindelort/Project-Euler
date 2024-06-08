from util.util import timing, format_number
from scripts.abstract_problem import Problem


class ProblemXXX(Problem):
    def __init__(self, **kwargs):
        super().__init__()

        if "arg" not in kwargs.keys():
            raise ValueError("arg not specified")

        self.answer, self.time_taken = self.solve(arg=kwargs["arg"])

        self.detailed_answer = f" is {format_number(self.answer)}"

    @timing
    def solve(self, **kwargs):
        pass


if __name__ == "__main__":
    problem = ProblemXXX()
    problem.print_problem()
