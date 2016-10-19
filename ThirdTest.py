from Matcher import Matcher

input = open('Pattern_matcher-test-input.txt')
i = 0
pattern = None
toMatch = None
for line in input:
    if i == 0:
        pattern = line[:-2]
        i=1
    else:
        toMatch = line[:-2]
        i=0
        solver = Matcher()
        solver.initialize(pattern,toMatch)
        solver.removeExclamations()

print 'done'

