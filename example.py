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
    465,
    465,
    465,
    465,
    465,
    465,
    465,
    465
]
item_demand = [
    210431,
    421870,
    900736,
    328282,
    526742,
    61473,
    202263,
    920272,
    100152,
    110010
]
performance = [
    [
        8.3937,
        1.5089,
        3.8357,
        1.0760,
        6.6285,
        6.7657,
        2.8993,
        7.2082,
        4.7714,
        9.4289
    ],
    [
        5.0505,
        7.9969,
        6.3603,
        1.1884,
        5.2050,
        1.8446,
        7.5308,
        8.1169,
        5.7492,
        2.4995
    ],
    [
        3.8030,
        4.5367,
        9.2844,
        4.3827,
        8.6640,
        8.3940,
        7.9894,
        3.1682,
        9.1355,
        7.4614
    ],
    [
        1.1212,
        6.9113,
        6.0358,
        6.9799,
        1.9048,
        9.4824,
        4.8036,
        4.8937,
        5.6463,
        3.3779
    ],
    [
        7.8070,
        9.7862,
        7.6024,
        7.9656,
        1.7338,
        3.2447,
        1.1811,
        9.6081,
        6.6832,
        8.1898
    ],
    [
        3.8961,
        7.7801,
        2.2977,
        7.1798,
        5.4545,
        5.4426,
        2.6278,
        8.6930,
        9.0606,
        5.6069
    ],
    [
        1.4258,
        1.5621,
        2.8331,
        2.8311,
        6.5411,
        5.9400,
        3.0936,
        4.9620,
        1.4312,
        3.3678
    ],
    [
        8.5487,
        3.6359,
        7.5217,
        5.7471,
        2.3022,
        8.7151,
        7.7622,
        6.7786,
        1.7582,
        9.7781
    ],
    [
        9.8951,
        1.1692,
        7.4622,
        9.5328,
        6.1451,
        5.4098,
        4.1895,
        4.4119,
        1.2437,
        8.9371
    ],
    [
        3.6835,
        7.8871,
        5.5981,
        8.8000,
        3.9282,
        6.1783,
        9.7410,
        2.5021,
        9.3576,
        6.5611
    ]
]


print('Optimization has begun...')
beginning = time()
sheudle, work_time, remains = association(performance, workers_limit, item_demand)
elapsed_time = time() - beginning

#Display and comparison
result_display(sheudle, work_time, remains, elapsed_time)
