Procedure for assigning tasks to employees for python 3.6 based on Hungarian algorithm.
Requires scipy package.
Usage:

Input:
    workers_limits:       [465, 180, ...]  workers work time limits
    item_demand:          [12, 7, ...]     how many each item is demanded
    performance_original: [[20.629, 12.252, ...], [17.849, 29.371, ...], ...] performance of each worker with each item
Output:
    plan:                 [9, 8, ...]      how many each type of item each worker is ordered to prepare
    item_demand:          [3, 0, ...]      how many items left
