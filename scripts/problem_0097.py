from util.util import timing, format_number
from scripts.abstract_problem import Problem


class Problem97(Problem):
    def __init__(self, **kwargs):
        super().__init__()

        if "factor" not in kwargs.keys():
            raise ValueError("factor not specified")

        if "base" not in kwargs.keys():
            raise ValueError("base not specified")

        if "exponent" not in kwargs.keys():
            raise ValueError("exponent not specified")

        if "target" not in kwargs.keys():
            raise ValueError("target not specified")

        self.answer, self.time_taken = self.solve(
            factor=kwargs["factor"],
            base=kwargs["base"],
            exponent=kwargs["exponent"],
            target=kwargs["target"],
        )

        self.detailed_answer = f"The last {format_number(kwargs['target'])} digits of {format_number(kwargs['factor'])} x {format_number(kwargs['base'])}^{format_number(kwargs['exponent'])} are {format_number(self.answer)}"

    @timing
    def solve(self, factor: int, base: int, exponent: int, target: int) -> int:
        return (factor * pow(base, exponent, target**target) + 1) % target**target


if __name__ == "__main__":
    problem = Problem97(factor=28_433, base=2, exponent=7_830_457, target=10)
    problem.print_problem()
