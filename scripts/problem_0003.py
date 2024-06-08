from util.util import timing, format_number
from scripts.abstract_problem import Problem


class Problem3(Problem):
    def __init__(self, **kwargs):
        super().__init__()

        if "number_to_factor" not in kwargs.keys():
            raise ValueError("number_to_factor not specified")

        self.answer, self.time_taken = self.solve(
            number_to_factor=kwargs["number_to_factor"]
        )

        self.detailed_answer = f"The largest prime factor of {format_number(kwargs['number_to_factor'])} is {format_number(self.answer)}"

    @timing
    def solve(self, number_to_factor: int) -> int:
        L = []
        m = number_to_factor
        while m != 1 or m != m:
            for i in range(2, m + 1):
                if m % i == 0:
                    L.append(i)
                    m = m // i
                    break
        return L[-1]


if __name__ == "__main__":
    problem = Problem3(number_to_factor=600_851_475_143)
    problem.print_problem()
