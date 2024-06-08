from util.util import timing, format_number
from scripts.abstract_problem import Problem


class Problem22(Problem):
    def __init__(self, **kwargs):
        super().__init__()

        self.answer, self.time_taken = self.solve()

        self.detailed_answer = f"The total of all the name score in the file is {format_number(self.answer)}"

    @timing
    def solve(self) -> int:
        lines = self.load_data_from_txt()
        lines.sort()
        score_tot = 0
        i = 0
        for line in lines:
            score = 0
            i += 1
            for lettre in line:
                if lettre != '"':
                    score += ord(lettre) % 64
            score = score * i
            score_tot += score
        return score_tot


if __name__ == "__main__":
    problem = Problem22()
    problem.print_problem()
