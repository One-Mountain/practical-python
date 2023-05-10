# pcost.py
#
# Exercise 1.27

cost = 0; 
with open('Work/Data/portfolio.csv', 'rt') as f: 
    headers = next(f).split(',')
    for line in f: 
        row = line.split(',')
        row[2] = row[2].strip()
        cost = cost + float(row[1]) * float(row[2])

print('The total cost is', cost)

