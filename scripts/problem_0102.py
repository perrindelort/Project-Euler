from shapely import Point, Polygon

from util.util import timing, format_number
from scripts.abstract_problem import Problem


class Problem102(Problem):
    def __init__(self, **kwargs):
        super().__init__()

        self.answer, self.time_taken = self.solve()

        self.detailed_answer = f"There are {format_number(self.answer)} triangles for which the interior contains the origin in the given file."

    @timing
    def solve(self) -> int:
        lines = self.load_data_from_txt(sep="\n")
        origin = Point(0, 0)
        counter = 0
        for idx, line in enumerate(lines):
            valeurs = [int(v) for v in line.strip().split(",")]
            point1 = Point(valeurs[0], valeurs[1])
            point2 = Point(valeurs[2], valeurs[3])
            point3 = Point(valeurs[4], valeurs[5])
            polygon = Polygon((point1, point2, point3))
            if polygon.contains(origin):
                counter += 1
        return counter


if __name__ == "__main__":
    problem = Problem102()
    problem.print_problem()
