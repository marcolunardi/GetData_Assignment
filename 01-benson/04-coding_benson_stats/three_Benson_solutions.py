from __future__ import division
import csv
from datetime import datetime
from collections import Counter


# MTA Data Challenges


# Challenge 1

# !curl -O http://web.mta.info/developers/data/nyct/turnstile/turnstile_150404.txt

with open('turnstile_150404.txt') as f:
    reader = csv.reader(f)
    rows = [[cell.strip() for cell in row] for row in reader]

assert rows.pop(0) == ['C/A', 'UNIT', 'SCP', 'STATION', 'LINENAME',
                       'DIVISION', 'DATE', 'TIME', 'DESC', 'ENTRIES',
                       'EXITS']

raw_readings = {}
for row in rows:
    raw_readings.setdefault(tuple(row[:4]), []).append(tuple(row[4:]))

# `raw_readings` is a solution to Challenge 1.


# Challenge 2

datetime_cumulative = {turnstile: [(datetime.strptime(date + time,
                                                      '%m/%d/%Y%X'),
                                    int(in_cumulative))
                                   for _, _, date, time,
                                       _, in_cumulative, _ in rows]
                       for turnstile, rows in raw_readings.items()}

for rows in datetime_cumulative.values():
    assert rows == sorted(rows)

datetime_count_times = {turnstile: [[rows[i][0],
                                     rows[i+1][1] - rows[i][1],
                                     rows[i+1][0] - rows[i][0]]
                                    for i in range(len(rows) - 1)]
                        for turnstile, rows in datetime_cumulative.items()}

all_counts = [count
              for rows in datetime_count_times.values()
              for _, count, _ in rows]
all_counts.sort()
print all_counts[-5:]
print all_counts[:1200]

all_times = [duration.seconds / 60 / 60
             for rows in datetime_count_times.values()
             for _, _, duration in rows]
print Counter(all_times).most_common(10)

datetime_counts = {turnstile: [(time, count)
                               for (time, count, _) in rows
                               if 0 <= count <= 5000]
                   for turnstile, rows in datetime_count_times.items()}

# `datetime_counts` is a solution to Challenge 2.

all_good_counts = [count
                   for rows in datetime_counts.values()
                   for _, count in rows]
print len(all_good_counts) / len(all_counts)
all_good_counts.sort()
print all_good_counts[-5:]
print all_good_counts[:5]


# Challenge 3

day_counts = {}
for turnstile, rows in datetime_counts.items():
    by_day = {}
    for time, count in rows:
        day = time.date()
        by_day[day] = by_day.get(day, 0) + count
    day_counts[turnstile] = sorted(by_day.items())

# `day_counts` is a solution to Challenge 3.
