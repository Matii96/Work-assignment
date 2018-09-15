#Import the toolbox
from scipy.optimize import linear_sum_assignment
from workflow import association
import numpy as np
import time as tm

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
            64.5387,
            64.2726,
            92.0575,
            10.7035,
            45.6990,
            12.2794,
            79.6026,
            78.5554,
            19.1367,
            34.3577
    ],
    [
            29.3246,
            68.5227,
            85.7498,
            48.3151,
            86.1658,
            82.2488,
            49.9020,
            30.0182,
            72.5656,
            73.2809
    ],
    [
            51.6773,
            63.9573,
            91.3176,
            29.8344,
            57.8287,
            54.7931,
            60.7185,
            85.2671,
            39.0684,
            54.3211
    ],
    [
            36.9607,
            28.8623,
            39.6236,
            74.4565,
            72.7463,
            28.8425,
            64.5220,
            26.0045,
            52.0936,
            65.7316
    ],
    [
            28.8841,
            19.0019,
            32.6792,
            55.8112,
            75.8791,
            30.1129,
            96.0381,
            13.1773,
            96.4880,
            51.3372
    ],
    [
            97.5875,
            70.8602,
            76.5311,
            44.4602,
            96.4024,
            94.8705,
            24.1381,
            39.5291,
            26.7923,
            33.5108
    ],
    [
            19.4013,
            79.9283,
            98.8105,
            32.5747,
            69.9104,
            31.4956,
            29.4260,
            99.0932,
            84.3591,
            90.8708
    ],
    [
            34.7138,
            95.6764,
            51.9325,
            83.0699,
            66.6400,
            66.2798,
            39.8745,
            92.9709,
            69.6369,
            97.3252
    ],
    [
            95.7878,
            89.4001,
            12.7382,
            76.2165,
            84.8735,
            17.8794,
            11.8801,
            37.1200,
            34.6086,
            45.6349
    ],
    [
            64.7271,
            55.1177,
            45.8869,
            97.4663,
            14.2333,
            34.7023,
            97.3908,
            58.3578,
            36.8379,
            98.4456
    ]
]

beginning = tm.time()

all_items = []
for i in range(0, len(sztuki)):
    for j in range(0, len(sztuki[i])):
        all_items.append(i)


elapsed_time = tm.time() - beginning

#Debug
wyprodukowane = []
for mebel in meble:
    wyprodukowane.append(0)

for i in range(0, len(plan)):
    print('%s (%.2fh):' % (pracownicy[i], przepracowane[i] / 60))
    for j in range(0, len(plan[i])):
        print('    %s: %d' % (meble[j], plan[i][j]))
        wyprodukowane[j] += plan[i][j]

print('Wyprodukowane / pozostale:')
for i in range(0, len(meble)):
    print('%s: %d / %d' % (meble[i], wyprodukowane[i], pozostale[i]))

print('Czas optymalizowania: %.3fs' % elapsed_time)
