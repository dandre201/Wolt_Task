import csv
import operator
import statistics


date = input("Please enter the start date? (yyyy-mm-dd) ")
startTime = input("Please enter the start time? (hours) ")
strCheck=date + 'T' + startTime
endTime=int(startTime)+1
vault = {}
reader = csv.reader(open('pickup_times.csv', 'rt'), delimiter=',')
sortedlist = sorted(reader, key=operator.itemgetter(0))


# this section of code takes the csv data that is in the sortedlist and create a list
# based on time that is input
for i in range(0, len(sortedlist)):
    if sortedlist[i][0] in vault:
        pass
    else:
        tmp_loc = sortedlist[i][0]
        vault[tmp_loc] = []
        for j in range(i+1, len(sortedlist)):
            if sortedlist[j][0] == tmp_loc:
                if sortedlist[j][1].startswith(strCheck) == True:
                    vault[tmp_loc].append(sortedlist[j][2])
            else:
                break

#this section of code gets the median and writes it to the csv file

csv_name = 'med times for ', date, ' at ', startTime, '-', endTime, '.csv'
with open(' '.join(map(str,(csv_name))),'w') as timescsv:
    times_writer = csv.writer(timescsv, delimiter=',')
    times_writer.writerow(['location_id', 'Median time'])
    for k,v in vault.items():
        if len(v) != 0:
            str1 = ','.join(v)
            listint = map(int, str1.split(','))
            getMed=statistics.median(map(int,listint))
            print('median for location', k ,' is :', getMed)
            times_writer.writerow([k, getMed])
