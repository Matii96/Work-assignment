#Import the toolbox
from scipy.optimize import linear_sum_assignment
import numpy as np

def association(performance_original, workers_limit, item_demand):
    items_count = len(item_demand)
    workers_count = len(performance_original)
    
    #Checking passed parameters
    if workers_count != len(workers_limit):
        raise ValueError('Workers count in performance_original does not match workers_limit')
    for worker in range(0, workers_count):
        if len(performance_original[worker]) != items_count:
            raise ValueError('items count in performance_original does not match item_demand')

    #Utility variables
    workers_limit = workers_limit.copy()
    item_demand = item_demand.copy()
    performance = []
    sheudle = []
    overworked_time = []
    cost_array_last = np.array([])
    result_workers_last, result_assignments_last = [], []

    #Copying performance array to prevent interfering into its values
    for worker_performance in performance_original:
        performance.append(worker_performance.copy())

    #Just for convenience
    #Saving highest performance value for further operations as threshold
    performance_threshold = 0
    for worker in range(0, workers_count):
        for item in range(0, items_count):
            performance_threshold = max(performance_threshold, performance[worker][item])
    performance_threshold += 1

    #Preparing array of planned activities
    for worker in workers_limit:
        worker_sheudle = []
        for item in item_demand:
            worker_sheudle.append(0)
        sheudle.append(worker_sheudle)
        overworked_time.append(0)

    #Iterating over assignment turns
    #Each turn consists of single example of each item
    lockup = False
    while True:
        #Generating requirement for turn considering demands
        items_in_turn = []
        for item in range(0, len(item_demand)):
            if item_demand[item] > 0:
                items_in_turn.append(item)

        #No more items to do
        if len(items_in_turn) == 0:
            return sheudle, item_demand, overworked_time

        #Iterating over items in turn
        while len(items_in_turn) > 0:

            #Checking available resources of worker
            #If any item execution time exceeds his free time left then change it to threshold
            for worker in range(0, workers_count):

                #Omitting workers with no time for anything
                if workers_limit[worker] == -1:
                    continue

                remove_worker = True
                free_time = workers_limit[worker] - overworked_time[worker]
                for item in range(0, items_count):
                    if performance[worker][item] > free_time:
                        performance[worker][item] = performance_threshold
                    if performance[worker][item] < performance_threshold:
                        remove_worker = False

                #In case of no time for anything mark it in workers_limit
                if remove_worker:
                    workers_limit[worker] = -1

            #No more free workers to do any task
            if all(limit == -1 for limit in workers_limit):
                return sheudle, item_demand, overworked_time

            #Generating cost array to optimise
            #Each row is list of performances of current worker with each demanded item in turn
            cost = []
            workers_in_turn = []

            for worker in range(0, workers_count):

                #Omitting workers with no time for anything
                if workers_limit[worker] == -1:
                    continue

                #Checking if worker has time for any of items left in turn
                for item_in_turn in items_in_turn:
                    if performance[worker][item_in_turn] < performance_threshold:
                        worker_performance = []
                        for item_in_turn in items_in_turn:
                            worker_performance.append(performance[worker][item_in_turn])
                        workers_in_turn.append(worker)
                        cost.append(worker_performance)
                        break

            #No worker has time for any item in turn
            if len(cost) == 0:

                #Check for repeated situation that indicates loop stuck
                if lockup:
                    return sheudle, item_demand, overworked_time
                lockup = True
                break

            #No stuck at this moment
            lockup = False

            cost_array = np.array(cost)
            result_workers, result_assignments = [], []

            #Just for omitting needless optimisations
            #Comparing new cost array and one from previous turn
            if np.array_equal(cost_array, cost_array_last):
                result_workers, result_assignments = result_workers_last, result_assignments_last
            else:

                #Arrays are different, launching new optimisation
                cost_array_last = np.copy(cost_array)
                result_workers, result_assignments = linear_sum_assignment(cost_array)
                result_workers_last, result_assignments_last = result_workers.copy(), result_assignments.copy()

            #print('cost:', np.array(cost)[result_workers, result_assignments].sum())

            #Reading result of optimisations
            for key in range(0, len(result_assignments)):
                current_worker = workers_in_turn[result_workers[key]]
                current_item = items_in_turn[result_assignments[key]]

                #Worker can be assigned to tast that exceeds his free time
                #In this case values remain unchanged
                if performance[current_worker][current_item] < performance_threshold:

                    #Adding item to worker
                    sheudle[current_worker][current_item] += 1

                    #Marking item for delete
                    items_in_turn[result_assignments[key]] = -1

                    #Decreasing the demand
                    item_demand[current_item] -= 1

                    #Increasing worker's overworked time
                    overworked_time[current_worker] += performance[current_worker][current_item]

            #Removing all assigned items in current turn
            items_in_turn = [f for f in items_in_turn if f != -1]
