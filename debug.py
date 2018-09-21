#Import the toolbox
from workflow import association
from time import time
from itertools import permutations

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

def generate_workers_permutations(workers_count, length):
    if length == 1:
        return list(permutations(range(0, workers_count)))

    result = []
    permutation_new = list(permutations(range(0, workers_count)))
    permutations_remaining = generate_workers_permutations(workers_count, length-1)
    for permutation_remaining in permutations_remaining:
        for permutation in permutation_new:
            new_row = list(permutation_remaining)
            for worker in permutation:
                new_row.append(worker)
            result.append(new_row)

    return result

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
'''
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
'''
item_demand = [
    81,
    20,
    15,
    20,
    25,
    91,
    16,
    18,
    31,
    73
]
performance = [    [        4.8945,        3.2748,        5.0778,        7.7730,        9.0548,        3.0581,        7.5498,        5.8031,        7.5210,        7.8269    ],    [        9.3411,        6.9655,        8.7732,        3.1082,        1.5235,        4.2960,        8.7424,        5.1282,        4.8870,        9.7319    ],    [        7.1731,        9.1261,        4.9207,        1.5164,        6.5210,        6.2711,        4.9943,        8.9937,        4.7163,        8.7826    ],    [        7.6469,        5.5075,        5.5958,        9.6773,        2.4431,        5.2818,        1.9096,        8.7702,        4.8722,        9.2414    ],    [        9.9862,        3.2304,        3.8749,        5.6981,        9.8662,        4.4804,        4.0292,        6.5528,        5.0631,        4.2267    ],    [        2.7662,        7.6085,        6.7360,        9.1811,        1.2319,        9.2128,        7.0916,        8.7801,        2.5591,        3.4265    ],    [        2.7804,        4.4481,        6.0374,        6.9376,        4.9489,        5.2904,        5.3885,        2.1825,        4.8670,        3.2077    ],    [        4.6808,        8.7586,        2.3939,        2.7038,        4.4127,        1.4966,        6.8432,        1.6124,        4.3740,        4.8159    ],    [        9.6666,        9.6614,        6.4194,        3.0977,        1.4935,        3.9748,        6.4627,        6.0242,        6.4353,        3.7138    ],    [        8.3750,        2.6110,        5.7979,        5.9424,        4.0942,        5.6939,        5.8809,        2.6794,        9.4486,        7.3518    ]]

print('Optimization has begun...')
beginning = time()
sheudle, work_time, remains = association(performance, workers_limit, item_demand)
elapsed_time = time() - beginning

#Display and comparison
result_display(sheudle, work_time, remains, elapsed_time)
exit()

#Dump
print('Dump optimization has begun...')
beginning = time()
items_all = []
for i in range(0, len(item_demand)):
    for j in range(0, item_demand[i]):
        items_all.append(i)
'''
workers_all = []
for i in range(0, (len(items_all) // len(workers_limit)) + 1):
    for w in range(0, len(workers_limit)):
        workers_all.append(w)

workers_permutations = list(permutations(workers_all))
'''

workers_permutations = generate_workers_permutations(len(workers_limit), (len(items_all) // len(workers_limit)) + 1)

cost_min = None
cost_min_id = 0
for i in range(0, len(workers_permutations)):
    cost = 0
    overwork = False
    overworked_time = [0] * len(workers_limit)

    for item in range(0, len(items_all)):
        worker = workers_permutations[i][item]

        cost += performance[worker][items_all[item]]
        overworked_time[worker] += performance[worker][items_all[item]]

        if overworked_time[worker] > workers_limit[worker]:
            overwork = True
            break

    #print('cost:', cost)

    if overwork:
        continue

    if cost_min is None or cost < cost_min:
        cost_min = cost
        cost_min_id = i
elapsed_time = time() - beginning
workers_combination = workers_permutations[cost_min_id]

#Gathering data
sheudle = []
work_time = []
remains = item_demand.copy()
for worker in workers_limit:
    worker_sheudle = []
    for item in item_demand:
        worker_sheudle.append(0)
    sheudle.append(worker_sheudle)
    work_time.append(0)

for i in range(0, len(items_all)):
    worker = workers_combination[i]
    item = items_all[i]

    remains[item] -= 1
    sheudle[worker][item] += 1
    work_time[worker] += performance[worker][item]

result_display(sheudle, work_time, remains, elapsed_time)
