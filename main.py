#Import the toolbox
from scipy.optimize import linear_sum_assignment
from workflow import association
import numpy as np
import time
import math

pracownicy = [
    'p100000179',
    'p100000125',
    'p100000151',
    'p100000181',
    'p100000154',
    'p100000127',
    'p100000165',
    'p100000139',
    'p100000185',
    'p100000320'
]
limit = [
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
meble = [
    'm210',
    'm211',
    'm212',
    'm213',
    'm214',
    'm215',
    'm216',
    'm217',
    'm218',
    'm219',
]
sztuki = [
    200,
    24,
    17,
    2,
    29,
    30,
    12,
    5,
    18,
    29
]
wydajnosc = [
    [
            88.9200,
            95.8226,
            51.6692,
            66.7275,
            84.1778,
            37.3701,
            66.6339,
            20.0398,
            89.0651,
            86.0374
    ],
    [
            38.7854,
            2.1763,
            27.1525,
            4.5553,
            44.5514,
            87.5395,
            15.3913,
            44.4446,
            15.0542,
            90.0296
    ],
    [
            6.0577,
            17.9380,
            73.5791,
            40.0863,
            16.9712,
            24.1820,
            16.4183,
            43.1429,
            26.7845,
            61.1563
    ],
    [
            76.7273,
            31.3102,
            8.5219,
            39.8249,
            92.7980,
            99.5841,
            2.4195,
            83.9361,
            94.0864,
            95.5888
    ],
    [
            69.0936,
            1.6665,
            44.0379,
            63.1157,
            73.2806,
            99.7739,
            95.3264,
            61.2714,
            81.7525,
            82.9003
    ],
    [
            47.9313,
            13.5123,
            62.6428,
            46.7067,
            11.6701,
            93.5324,
            90.4098,
            3.7034,
            11.8908,
            11.3483
    ],
    [
            19.7785,
            81.9193,
            74.7744,
            8.4926,
            57.5639,
            77.1746,
            10.6597,
            78.0319,
            8.0148,
            28.1802
    ],
    [
            50.6366,
            52.2734,
            32.3661,
            74.4815,
            94.7644,
            3.6625,
            48.6794,
            32.0321,
            69.0096,
            67.6901
    ],
    [
            45.1958,
            13.2663,
            73.4919,
            18.9836,
            43.2314,
            3.5651,
            24.6316,
            92.3761,
            8.6233,
            78.9346
    ],
    [
            20.6385,
            87.3686,
            42.1846,
            3.8758,
            72.6223,
            30.1311,
            94.9940,
            65.0571,
            13.4978,
            28.6959
    ]
]

print('Rozpoczęto optymalizację...')
beginning = time.time()
plan, pozostale, przepracowane = association(wydajnosc, limit, sztuki)
elapsed_time = time.time() - beginning

#Debug
wyprodukowane = []
for mebel in meble:
    wyprodukowane.append(0)

for i in range(0, len(plan)):
    minuty, godziny = math.modf(przepracowane[i] / 60)
    #print('%s (%d:%02d):' % (pracownicy[i], godziny, minuty * 60))
    print('%s (%.0f/%.0f):' % (pracownicy[i], przepracowane[i], limit[i]))
    for j in range(0, len(plan[i])):
        print('    %s: %d' % (meble[j], plan[i][j]))
        wyprodukowane[j] += plan[i][j]

print('Wyprodukowane / pozostale:')
for i in range(0, len(sztuki)):
    print('%s: %d / %d' % (sztuki[i], wyprodukowane[i], pozostale[i]))

print('Czas optymalizowania: %.3fs' % elapsed_time)
