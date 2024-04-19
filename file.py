import random
import timeit
import numpy as np

def T(segment_lengths, i, j):
    if i == j:
        return segment_lengths[i]
    total_length = 0
    for k in range(i, j + 1):
        total_length += segment_lengths[k]
    left_choice = T(segment_lengths, i + 1, j)
    right_choice = T(segment_lengths, i, j - 1)
    return total_length - min(left_choice, right_choice)

n_values = range(10, 20)  # The range of n values
num_trials = 5  # Number of trials to average
average_times = []

for n in n_values:
    trial_times = []
    for _ in range(num_trials):
        segments = [random.randint(1, 1000) for _ in range(n)]
        start_time = timeit.default_timer()
        T(segments, 0, n - 1)
        trial_times.append(timeit.default_timer() - start_time)
    average_times.append(np.mean(trial_times))

# Prepare data for the table
table_data = list(zip(n_values, average_times))

print(table_data)