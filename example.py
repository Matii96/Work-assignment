#Import the toolbox
from workflow import association
from time import time

def result_display(sheudle, work_time, remains, elapsed_time):
    done = []
    for item in remains:
        done.append(0)

    work_time_total = 0
    for i in range(0, len(sheudle)):
        print('worker%d (%.0f/%.0f):' % (i, work_time[i], workers_limit[i]))
        for j in range(0, len(sheudle[i])):
            print('    item%d: %d' % (j, sheudle[i][j]))
            done[j] += sheudle[i][j]
        work_time_total += work_time[i]

    print('Item: done / remaining:')
    for i in range(0, len(item_demand)):
        print('item%d: %d / %d' % (i, done[i], remains[i]))

    remains_total = 0
    for item_count in remains:
        remains_total += item_count
    print('Total items remaining: %d' % remains_total)

    print('Total work time: %.0f' % work_time_total)
    print('Elapsed time: %.3fs\n' % elapsed_time)

#Test data
workers_limit = [
    465,
    465,
    465
]
item_demand = [
    10,
    41,
    10,
    38,
    101
]
performance = [
    [
        8.3937,
        1.5089,
        3.8357,
        1.0760,
        6.6285
    ],
    [
        5.0505,
        7.9969,
        6.3603,
        1.1884,
        5.2050
    ],
    [
        3.8030,
        4.5367,
        9.2844,
        4.3827,
        8.6640
    ]
]

print('Optimization has begun...')
beginning = time()
sheudle, work_time, remains = association(performance, workers_limit, item_demand)
elapsed_time = time() - beginning

#Display and comparison
result_display(sheudle, work_time, remains, elapsed_time)
