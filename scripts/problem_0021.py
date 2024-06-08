from util.util import timing, format_number
from scripts.abstract_problem import Problem


class Problem21(Problem):
    def __init__(self, **kwargs):
        super().__init__()

        if "upper_bound" not in kwargs.keys():
            raise ValueError("upper_bound not specified")

        self.answer, self.time_taken = self.solve(upper_bound=kwargs["upper_bound"])

        self.detailed_answer = f"The sum of all amicable number under {format_number(kwargs['upper_bound'])} is {format_number(self.answer)}"

    @timing
    def solve(self, upper_bound: int) -> int:
        dictionaryDivisor = {}
        keys = [2] * upper_bound
        for i in range(2, upper_bound):
            keys[i] = i
            L = []
            for j in range(1, i // 2 + 1):
                if i % j == 0:
                    L.append(j)
            if L == []:
                dictionaryDivisor[i] = [i]
            else:
                dictionaryDivisor[i] = L
        amicableNumbers = []
        for key in keys:
            somme1 = sum(dictionaryDivisor.get(key))
            try:
                somme2 = sum(dictionaryDivisor.get(somme1))
                if somme2 == key and key != somme1:
                    if key not in amicableNumbers:
                        amicableNumbers.append(somme1)
                        if somme2 not in amicableNumbers:
                            amicableNumbers.append(somme2)
            except:
                pass
        return sum(amicableNumbers)


if __name__ == "__main__":
    problem = Problem21(upper_bound=10_000)
    problem.print_problem()
