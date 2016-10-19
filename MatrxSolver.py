import sys
import copy

class MatrxSolver:
    def __init__(self):
        self.A=[]
        self.bestIter = sys.maxint
        self.solution = []

    def initializea(self, a):
        self.A = a

    def populate(self, friends):
        temp = copy.deepcopy(friends)
        for f in range (0, friends.__len__()):
            if temp[f] != 0:
                for g in range(0, self.A.__len__()):
                    if self.A[f][g] != 0:
                        friends[g] = 1

        return friends

    def solvea(self):
        for i in range (0, self.A.__len__()):
            friends = [0]*self.A.__len__()
            friends[i] = 1
            iter = 1
            while sum(friends) < friends.__len__() and iter < 101:
                friends = self.populate(friends)
                iter += 1
            if self.bestIter >= iter and iter < 101:
                if iter < self.bestIter:
                    self.solution = []
                    self.bestIter = iter
                self.solution.append(i)





