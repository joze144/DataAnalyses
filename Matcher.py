class Matcher():
    def __init__(self):
        self.pattern = None
        self.toMatch = None
        self.exclamations = []

    def initialize(self, pattern, toMatch):
        self.pattern = pattern
        self.toMatch = toMatch



    def removeExclamations(self):
        first = True
        a=0
        b=0
        i=0
        for c in self.pattern:
            i+=1
            if c == "!" and first:
                a = i
                first = False
            elif c == "!" and not first:
                b=i
                self.exclamations.append([a,self.pattern[a:(b - 1)]])
                first = True

    def checkOutsideExclamations(self):
        i=0
        possibleSolutions=[]
        for n in range (0,self.exclamations.__len__()):
            patt = self.pattern[i:self.exclamations[n][0]]
            i=self.exclamations[n][0] + self.exclamations[n][1].__len__()






    def doMatch(self):
        self.removeExclamations()
        self.checkOutsideExclamations()

