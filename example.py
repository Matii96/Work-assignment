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
item_demand = [
    21043,
    42187,
    90076,
    32882,
    52642,
    61473,
    20263,
    92072,
    10052,
    11000
]
performance = [    [        0.0000,        2.0000,        0.0000,        8.0000,        9.0000,        9.0000,        3.0000,        0.0000,        2.0000,        4.0000    ],    [        9.0000,        3.0000,        4.0000,        1.0000,        0.0000,        3.0000,        3.0000,        8.0000,        6.0000,        7.0000    ],    [        4.0000,        3.0000,        3.0000,        7.0000,        0.0000,        5.0000,        5.0000,        4.0000,        2.0000,        3.0000    ],    [        1.0000,        4.0000,        0.0000,        1.0000,        2.0000,        4.0000,        7.0000,        1.0000,        9.0000,        2.0000    ],    [        9.0000,        2.0000,        3.0000,        8.0000,        7.0000,        7.0000,        2.0000,        7.0000,        1.0000,        1.0000    ],    [        9.0000,        7.0000,        4.0000,        5.0000,        0.0000,        1.0000,        6.0000,        4.0000,        9.0000,        9.0000    ],    [        8.0000,        5.0000,        7.0000,        5.0000,        0.0000,        7.0000,        3.0000,        2.0000,        8.0000,        5.0000    ],    [        7.0000,        5.0000,        7.0000,        7.0000,        9.0000,        3.0000,        2.0000,        2.0000,        6.0000,        7.0000    ],    [        8.0000,        4.0000,        8.0000,        0.0000,        3.0000,        5.0000,        5.0000,        8.0000,        6.0000,        0.0000    ],    [        2.0000,        2.0000,        3.0000,        6.0000,        7.0000,        6.0000,        5.0000,        8.0000,        5.0000,        0.0000    ]]

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
