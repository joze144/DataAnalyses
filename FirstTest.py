import sys
from MatrxSolver import MatrxSolver

T=0
A=[]

my_list = [line.split(' ') for line in open('Pass_the_message-test-input.txt')]
output = open("output.txt", "wb")

i=0
k=0
n=0
for row in my_list:
    if i==0:
        t=int(row[0])
        i+=1
    else:
        if k==0:
            k=int(row[0])
            n=k
        else:
            subrow = [0]*n
            for i in row:
                subrow[int(i)-1] = 1
            k-=1
            A.append(subrow)
            if k==0:
                solver = MatrxSolver()
                solver.initializea(A)
                solver.solvea()
                if solver.solution.__len__() == 0:
                    output.write("0")
                kh=0
                for s in solver.solution:
                    kh+=1
                    if kh == solver.solution.__len__():
                        output.write("%d" % (s + 1))
                    else:
                        output.write("%d " % (s + 1))
                output.write("\n")
                A=[]

print ('done')


