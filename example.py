#Import the toolbox
from workflow import association
from time import time
from itertools import permutations

def result_display(sheudle, work_time, remains, elapsed_time, workers, items):
    done = []
    for item in items:
        done.append(0)

    work_time_total = 0
    for i in range(0, len(sheudle)):
        print('%s (%.0f/%.0f):' % (workers[i], work_time[i], workers_limit[i]))
        for j in range(0, len(sheudle[i])):
            print('    %s: %d' % (items[j], sheudle[i][j]))
            done[j] += sheudle[i][j]
        work_time_total += work_time[i]

    print('Item: done / remaining:')
    for i in range(0, len(item_demand)):
        print('%s: %d / %d' % (items[i], done[i], remains[i]))

    print('Total work time: %.0f' % work_time_total)
    print('Elapsed time: %.3fs\n' % elapsed_time)

#Test data
workers_limit = [
    465,
    465,
    465
]
item_demand = [
    210,
    132,
    24,
    19,
    58
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
beginning = time()
sheudle, work_time, remains = association(performance, workers_limit, item_demand)
elapsed_time = time() - beginning

#Display and comparison
workers = [
    'p100000001',
    'p100000002',
    'p100000003'
]
items = [
    'm210',
    'm211',
    'm212',
    'm213',
    'm214'
]
result_display(sheudle, work_time, remains, elapsed_time, workers, items)
exit()
#Dump
print('Dump optimization has begun...')
beginning = time()
items_all = []
for i in range(0, len(item_demand)):
    for j in range(0, item_demand[i]):
        items_all.append(i)

workers_all = []
for i in range(0, (len(items_all) // len(workers_limit)) + 1):
    for w in range(0, len(workers_limit)):
        workers_all.append(w)

workers_permutations = list(permutations(workers_all))


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

result_display(sheudle, work_time, remains, elapsed_time, workers, items)
