from util.util import timing, format_number
from scripts.abstract_problem import Problem


class Problem5(Problem):
    def __init__(self, **kwargs):
        super().__init__()

        if "upper_bound" not in kwargs.keys():
            raise ValueError("upper_bound not specified")

        self.answer, self.time_taken = self.solve(upper_bound=kwargs["upper_bound"])

        self.detailed_answer = f"The smallest positive integer that is evenly divisible with no remainder by all the numbers from 1 to {format_number(kwargs['upper_bound'])} is {format_number(self.answer)}"

    # TODO : move function to utils
    def prime_factors(self, n):
        L = []
        m = n
        while m != 1 or m != m:
            for i in range(2, m + 1):
                if m % i == 0:
                    L.append(i)
                    m = m // i
                    break
        return L

    @timing
    def solve(self, upper_bound: int) -> int:
        L = [2]
        for i in range(3, upper_bound + 1):
            L2 = self.prime_factors(i)
            for facteur in L2:
                if facteur in L:
                    if L2.count(facteur) > L.count(facteur):
                        while L2.count(facteur) != L.count(facteur):
                            L.append(facteur)
                else:
                    L.append(facteur)
        p = 1
        for facteur in L:
            p = p * facteur
        return p


if __name__ == "__main__":
    problem = Problem5(upper_bound=20)
    problem.print_problem()
