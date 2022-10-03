import csv
    
infile = open("steps.csv","r")
csvfile = csv.reader(infile, delimiter=",")
outfile = open("avg_steps.csv","w")
outfile.write("Month,Steps\n")

months = ['',"January","February","March","April","May","June","July","August","September","October","November","December"]

totalSteps = 0
month = 1
dayCount = 0

next(csvfile)

for rec in csvfile:
    if int(rec[0]) == month:
        totalSteps += int(rec[1])
        dayCount += 1

    else: 
        avgSteps = round(totalSteps/dayCount,2)
        outfile.write(monthNames[month]+','+str(avgSteps)+"\n")
        totalSteps = int(rec[1])
        dayCount = 1
        month += 1

avgSteps = round(totalSteps/dayCount,2)
outfile.write(monthNames[month]+','+str(avgSteps)+"\n")

outfile.close()
