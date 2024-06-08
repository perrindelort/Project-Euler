import math

from util.util import timing, format_number
from scripts.abstract_problem import Problem


class Problem7(Problem):
    def __init__(self, **kwargs):
        super().__init__()

        if "prime_rank" not in kwargs.keys():
            raise ValueError("prime_rank not specified")

        self.answer, self.time_taken = self.solve(prime_rank=kwargs["prime_rank"])

        self.detailed_answer = f"The {format_number(kwargs['prime_rank'])}st prime is {format_number(self.answer)}"

    # TODO : move function to utils
    def isPrime(self, n):
        if n == 1:
            return False
        elif n == 2:
            return True
        for i in range(2, math.ceil(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    @timing
    def solve(self, prime_rank: int) -> int:
        L = []
        i = 2
        while len(L) != prime_rank:
            if self.isPrime(i):
                L.append(i)
            i += 1
        return L[-1]


if __name__ == "__main__":
    problem = Problem7(prime_rank=10_001)
    problem.print_problem()
