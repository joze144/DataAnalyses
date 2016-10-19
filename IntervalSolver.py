from datetime import date, datetime, time
import math

class IntervalSolver():
    def __init__(self):
        self.intervals = []
        self.date = None
        self.bestIntersection = 0
        self.earnings = 0


    def intersectionSolve(self):
        for i in self.intervals:
            t = i[0]
            temp = 0
            for inside in self.intervals:
                if inside[1] > t and inside[0] <= t:
                    temp += 1
            if temp > self.bestIntersection:
                    self.bestIntersection = temp

            self. earnings += self.moneyEarnings(i)


    def moneyEarnings(self, interval):
        diff = interval[1] - interval[0]
        hours, remainder = divmod(diff.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        earnings = 0
        if hours:
            earnings += hours*2
            earnings += math.ceil(minutes / 15.0) * 0.5
            i = minutes % 15
            if i == 0 and seconds > 0:
                earnings += 0.5
        else:
            earnings = 2

        return earnings

    def fillIntervals(self, interval):
        self.intervals = interval