#Import the toolbox
from workflow import association
import time
import math

workers_limit = [
    465,
    465,
    465
]
item_demand = [
    200,
    24,
    17,
    2,
    29
]
performance = [
    [
        88.9200,
        95.8226,
        51.6692,
        66.7275,
        84.1778
    ],
    [
        38.7854,
        2.1763,
        27.1525,
        4.5553,
        44.5514
    ],
    [
        6.0577,
        17.9380,
        73.5791,
        40.0863,
        16.9712
    ]
]

print('Optimization has begun...')
beginning = time.time()
sheudle, work_time, remains = association(performance, workers_limit, item_demand)
elapsed_time = time.time() - beginning

#Display
workers = [
    'p100000179',
    'p100000125',
    'p100000151'
]
items = [
    'm210',
    'm211',
    'm212',
    'm213',
    'm214'
]

done = []
for item in items:
    done.append(0)

for i in range(0, len(sheudle)):
    print('%s (%.0f/%.0f):' % (workers[i], work_time[i], workers_limit[i]))
    for j in range(0, len(sheudle[i])):
        print('    %s: %d' % (items[j], sheudle[i][j]))
        done[j] += sheudle[i][j]

print('Item: done / remaining:')
for i in range(0, len(item_demand)):
    print('%s: %d / %d' % (items[i], done[i], remains[i]))

print('Elapsed time: %.3fs' % elapsed_time)
