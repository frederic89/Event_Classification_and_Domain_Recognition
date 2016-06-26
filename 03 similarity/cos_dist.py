__author__ = 'gyq-mac'

import numpy as np
import csv

a = np.array([1, 0.0000, 0.9963, 0.0000, 0.0000, 0.0025, 0.0000, 0.0000, 0.0000, 0.0000, 0.0001, 0.0008, 0.0001])

reader = csv.reader(file('output.csv', 'rb'))
group = []
for line_n in reader:
    line_n = np.asarray(line_n, dtype=np.float32)
    group.append(line_n)

idx = {}
for vector in group:
    cos = np.dot(a, vector[:13]) / (np.linalg.norm(a) * np.linalg.norm(vector[:12]))
    if cos > 0.95:
        idx[vector[13]] = cos
print(idx)

