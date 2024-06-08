import numpy as np

from util.util import timing, format_number
from scripts.abstract_problem import Problem


class Problem12(Problem):
    def __init__(self, **kwargs):
        super().__init__()

        if "threshold" not in kwargs.keys():
            raise ValueError("threshold not specified")

        self.answer, self.time_taken = self.solve(threshold=kwargs["threshold"])

        self.detailed_answer = f"The first triangle number to have over {format_number(kwargs['threshold'])} divisors is {format_number(self.answer)}"

    # TODO : move function to utils
    def compterDiviseurs(self, n):
        produit = 1
        for facteur in self.facteursPremiers(n).values():
            produit = produit * (facteur + 1)
        return produit

    def facteursPremiers(self, n):
        L = {}
        m = n
        while m != 1 or m != m:
            for i in range(2, m + 1):
                if m % i == 0:
                    try:
                        L.update({i: L.get(i) + 1})
                    except:
                        L[i] = 1
                    m = m // i
                    break
        return L

    @timing
    def solve(self, threshold: int) -> int:
        i = 1
        s = 1
        n = 0
        while n < threshold:
            n = self.compterDiviseurs(s)
            if n >= threshold:
                return s
            i += 1
            s += i


if __name__ == "__main__":
    problem = Problem12(threshold=500)
    problem.print_problem()
