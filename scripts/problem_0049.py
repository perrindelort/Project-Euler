from primePy import primes
from typing import Tuple

from util.util import timing, format_number
from util.funct import is_permutation
from scripts.abstract_problem import Problem


class Problem49(Problem):
    def __init__(self, **kwargs):
        super().__init__()

        self.answer, self.time_taken = self.solve()

        self.detailed_answer = f"The other other 4-digit increasing sequence solution to the given problem is {format_number(self.answer[1])} {format_number(self.answer[2])} {format_number(self.answer[3])} which forms by concatenation {format_number(self.answer[0])}"

        # We returned 4 values for the detailed_answer
        self.answer = self.answer[0]

    @timing
    def solve(self) -> Tuple[int, int, int, int]:
        primes_list = primes.between(1000, 9999)
        dictionary = {}
        for index1 in range(len(primes_list)):
            prime1 = primes_list[index1]
            if prime1 > 4000:
                break
            for index2 in range(index1 + 1, len(primes_list)):
                prime2 = primes_list[index2]
                if is_permutation(str(prime1), str(prime2)):
                    if dictionary.get(prime1) == None:
                        dictionary[prime1] = [prime2]
                    else:
                        dictionary[primes_list[index1]].append(prime2)
        for key in dictionary.keys():
            if key == 1487:
                continue
            for prime1 in dictionary.get(key):
                for prime2 in dictionary.get(key):
                    if prime1 - key == prime2 - prime1:
                        return (
                            int(str(key) + str(prime1) + str(prime2)),
                            key,
                            prime1,
                            prime2,
                        )


if __name__ == "__main__":
    problem = Problem49()
    problem.print_problem()
