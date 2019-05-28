# Description
Procedure for assigning tasks to employees for python 3.6 based on Hungarian algorithm. Requires scipy package.

# Usage
-Inputs:
  - performance_original: [[20.629, 12.252, ...], [17.849, 29.371, ...], ...] performance of each worker with each item
  - workers_limits:       [465, 180, ...]  workers work time limits
  - item_demand:          [12, 7, ...]     how many each item is demanded
-Outputs:
  -scheudle:              [9, 8, ...]      how many each type of item each worker is ordered to prepare
  -overworked_time:       [459.5, 179.2]   work time of each worker
  -item_demand:           [3, 0, ...]      how many items left
