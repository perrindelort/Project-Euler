from util.util import timing, format_number
from scripts.abstract_problem import Problem


class Problem16(Problem):
    def __init__(self, **kwargs):
        super().__init__()

        if "power_of_2" not in kwargs.keys():
            raise ValueError("power_of_2 not specified")

        self.answer, self.time_taken = self.solve(power_of_2=kwargs["power_of_2"])

        self.detailed_answer = f"The sum of the digits of 2^{kwargs['power_of_2']} is {format_number(self.answer)}"

    @timing
    def solve(self, power_of_2: int) -> int:
        nombre = 2**power_of_2
        string = str(nombre)
        somme = 0
        for chiffre in string:
            somme += int(chiffre)
        return somme


if __name__ == "__main__":
    problem = Problem16(power_of_2=1_000)
    problem.print_problem()
