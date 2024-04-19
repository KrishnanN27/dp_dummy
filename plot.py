import random
import timeit
import matplotlib.pyplot as plt

def T(segment_lengths, i, j):
    if i == j:
        return segment_lengths[i]
    total_length = sum(segment_lengths[i:j+1])
    left_choice = T(segment_lengths, i + 1, j)
    right_choice = T(segment_lengths, i, j - 1)
    return total_length - min(left_choice, right_choice)

n_values = range(10, 19) 
times = []

for n in n_values:
    segments = [random.randint(1, 1000) for _ in range(n)]
    start_time = timeit.default_timer()
    T(segments, 0, n - 1)
    times.append(timeit.default_timer() - start_time)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(n_values, times, marker='o', linestyle='-')
plt.xlabel('Size of n (number of segments)')
plt.ylabel('Runtime (seconds)')
plt.title('Runtime Analysis of the Timber Problem Algorithm')
plt.grid(True)
plt.show()
