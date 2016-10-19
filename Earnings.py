import math
from datetime import datetime, time, timedelta

class Earnings():
    def __init__(self):
        self.end = None
        self.ent = None
        self.exd = None
        self.ext = None
        self.earnings = 0

    def initialize(self, end, ent, exd, ext):
        self.end = end
        self.ent = ent
        self.exd = exd
        self.ext = ext

    def moneyEarnings(self):
        diff = datetime.strptime("00:00:00", "%H:%M:%S") - datetime.strptime("00:00:00", "%H:%M:%S")
        while self.end < self.exd:
            diff += datetime.strptime("23:59:59", "%H:%M:%S") - self.ent
            self.ent = datetime.strptime("00:00:00", "%H:%M:%S")
            self.end += timedelta(days=1)

        diff += self.ext - self.ent
        hours, remainder = divmod(diff.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        if hours:
            self.earnings += hours*2
            self.earnings += math.ceil(minutes / 15.0) * 0.5
            i = minutes % 15
            if i == 0 and seconds > 0:
                self.earnings += 0.5
        else:
            self.earnings += 2


