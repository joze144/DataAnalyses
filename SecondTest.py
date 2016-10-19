from datetime import date, datetime, time, timedelta
from IntervalSolver import IntervalSolver
from Earnings import Earnings

earningsPerDay = dict()
listOfDays=[]
file = open('Car_Park-test-input.txt')
Days=dict()
firstline = 0
for line in file:
    line = line.strip()
    if firstline == 0:
        firstline = 1
        continue
    else:
        l = line.split(' ')
        enterdate = l[0]
        entertime = l[1]
        exitdate = l[3]
        exittime = l[4]
        fuuuu = enterdate[-4:]
        fuuuu2 = exitdate[-4:]
        enterdate = enterdate[:-4] + str(int(fuuuu) + 400)
        exitdate = exitdate[:-4] + str(int(fuuuu2) + 400)
        end = datetime.strptime(enterdate, "%d.%m.%Y")
        ent = datetime.strptime(entertime, "%H:%M:%S")
        exd = datetime.strptime(exitdate, "%d.%m.%Y")
        ext = datetime.strptime(exittime, "%H:%M:%S")

        earn = Earnings()
        earn.initialize(end, ent, exd, ext)
        earn.moneyEarnings()
        if exd not in earningsPerDay:
            earningsPerDay[exd] = earn.earnings
        else:
            earningsPerDay[exd] += earn.earnings

        while end < exd:
            #earned =
            if end not in Days:
                Days[end] = []
                listOfDays.append(end)
            Days[end].append([ent, datetime.strptime("23:59:59", "%H:%M:%S")])
            ent = datetime.strptime("00:00:00", "%H:%M:%S")
            end += timedelta(days=1)


        if end not in Days:
            Days[end] = []
            listOfDays.append(end)
        Days[end].append([ent, ext])





output = open("output_second.txt", "wb")
totalEarnings = 0
for key in earningsPerDay:
    totalEarnings += earningsPerDay[key]
peakDay = None
peakCars = 0
listOfDays = sorted(listOfDays)
for key in listOfDays:
    solver = IntervalSolver()
    solver.fillIntervals(Days[key])
    solver.intersectionSolve()
    if solver.bestIntersection > peakCars:
        peakCars = solver.bestIntersection
        peakDay = key

    if key in earningsPerDay:
        outdate = datetime.strftime(key, "%d.%m.%Y")
        outdate = outdate[:-4] + str(int(outdate[-4:]) - 400)
        output.write("%s " % outdate)
        output.write("%d " % solver.bestIntersection)
        output.write("%.1f" % earningsPerDay[key])
        output.write("\n")

outdate = datetime.strftime(peakDay, "%d.%m.%Y")
outdate = outdate[:-4] + str(int(outdate[-4:]) - 400)
output.write("PEAK %d AT %s" % (peakCars, outdate))
output.write("\n")
output.write("TOTAL %.1f" % totalEarnings)