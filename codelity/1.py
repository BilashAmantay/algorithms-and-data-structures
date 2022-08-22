import datetime
import os
S = open('1.txt').read()
print(S.splitlines())

Slines = S.splitlines()

photoes = []
cities = []
uniqCities = set()
cityCounts = {}
dateTimesStr = []
dateTime = []
records = []
results = []

for idx,line in enumerate(Slines):
    record = line.split(', ')
    data  = {}
    data['idx'] = idx
    data['photo'] = record[0]
    data['city'] = record[1]
    data['dateTimesStr'] = record[2]
    data['dateTime'] = datetime.datetime.strptime(record[2], '%Y-%m-%d %H:%M:%S')
    records.append(data)

    if record[1] not in cityCounts:
        cityCounts[record[1]] = 1
    else:
        cityCounts[record[1]] += 1

sortedRecord = sorted(records, key=lambda x:x['dateTime'])
orderDict = {}

for city in cityCounts.keys():
    filtered = filter(lambda x:x['city'] ==  city, sortedRecord)
    numDigits = len(str(cityCounts[city]))

    order=0
    for f in filtered:
        order+=1
        orderSuffix = str(order).zfill(numDigits)
        orderDict[f['idx']] = orderSuffix


for data in records:
    splitedName =  os.path.splitext(data['photo'])
    newName = splitedName[0] + '_' + data['city'] + orderDict[data['idx']] + splitedName[1]
    print(newName)
    results.append(newName)


    

