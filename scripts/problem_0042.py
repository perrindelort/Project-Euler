from util.util import timing, format_number
from scripts.abstract_problem import Problem


class Problem42(Problem):
    def __init__(self, **kwargs):
        super().__init__()

        self.answer, self.time_taken = self.solve()

        self.detailed_answer = f"There are {format_number(self.answer)} triangle words in the given text file"

    @timing
    def solve(self) -> int:
        lines = self.load_data_from_txt()
        score_lines = []
        for line in lines:
            score = 0
            for letter in line:
                if letter != '"':
                    score += ord(letter) % 64
            score_lines.append(score)
        score_lines.sort()
        triangle_numbers = [1]
        supremum = score_lines[-1]
        while triangle_numbers[-1] < supremum:
            triangle_numbers.append(triangle_numbers[-1] + len(triangle_numbers) + 1)
        count_triangle_numbers = 0
        for score in score_lines:
            if score in triangle_numbers:
                count_triangle_numbers += 1
        return count_triangle_numbers


if __name__ == "__main__":
    problem = Problem42()
    problem.print_problem()
