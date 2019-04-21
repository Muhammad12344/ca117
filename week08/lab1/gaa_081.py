class Score(object):

    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points

    def point(self):
        return self.goals * 3 + self.points

    def __str__(self):
        return "{} goal(s) and {} point(s)".format(self.goals, self.points)

    def __eq__(self, other):
        return self.point() == other.point()

    def __gt__(self, other):
        return self.point() > other.point()

    def __lt__(self, other):
        return self.point() < other.point()

    def __ge__(self, other):
        return self.point() >= other.point()

    def __le__(self, other):
        return self.point() <= other.point()

    def __add__(self, other):
        return Score(self.goals + other.goals, self.points + other.points)

    def __sub__(self, other):
        return Score(self.goals - other.goals, self.points - other.points)

    def __iadd__(self, other):
        z = self + other
        self.goals, self.points = z.goals, z.points
        return self

    def __isub__(self, other):
        z = self - other
        self.goals, self.points = z.goals, z.points
        return self
