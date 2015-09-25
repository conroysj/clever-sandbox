from collections import defaultdict
import csv
d = defaultdict(int)
sumofclasses = 0
sumofstudents = 0
f = open('enrollments.csv', 'rU')
csv_f = csv.reader(f)
for row in csv_f:
  try:
    sid = int(row[2])
  except ValueError:
    continue
  d[sid] += 1
print d
for k,v in d.iteritems():
  sumofclasses += 1
  sumofstudents += v
print sumofstudents
print sumofclasses

f.close()
