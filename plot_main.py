import matplotlib.pyplot as plt
import random
import timeit

# Naive recursive algorithm (already provided)
def T(segment_lengths, i, j):
    if i == j:
        return segment_lengths[i]
    total_length = sum(segment_lengths[i:j+1])
    left_choice = T(segment_lengths, i + 1, j)
    right_choice = T(segment_lengths, i, j - 1)
    return total_length - min(left_choice, right_choice)

# Dynamic programming algorithm (provided earlier)
def T_dp(segment_lengths):
    n = len(segment_lengths)
    prefix_sum = [0]
    dp = [[0] * n for _ in range(n)]
    
    for i, length in enumerate(segment_lengths):
        prefix_sum.append(prefix_sum[-1] + length)
        dp[i][i] = length  
    
    for length in range(2, n + 1):  
        for i in range(n - length + 1):
            j = i + length - 1
            total_length = prefix_sum[j + 1] - prefix_sum[i]
            dp[i][j] = total_length - min(dp[i + 1][j], dp[i][j - 1])
    
    return dp[0][n - 1]

# Measuring runtimes for both algorithms
n_values_recursive = range(10, 19)  # smaller range for recursive due to exponential complexity
n_values_dp = range(10, 201, 10)  # larger range for dynamic programming due to better complexity
times_recursive = []
times_dp = []

# Measure runtime for the naive recursive algorithm
for n in n_values_recursive:
    segments = [random.randint(1, 1000) for _ in range(n)]
    start_time = timeit.default_timer()
    T(segments, 0, n - 1)
    times_recursive.append(timeit.default_timer() - start_time)

# Measure runtime for the dynamic programming algorithm
for n in n_values_dp:
    segments = [random.randint(1, 1000) for _ in range(n)]
    start_time = timeit.default_timer()
    T_dp(segments)
    times_dp.append(timeit.default_timer() - start_time)

# Plot the results
plt.figure(figsize=(12, 8))
plt.plot(n_values_recursive, times_recursive, marker='o', linestyle='-', label='Naive Recursive')
plt.plot(n_values_dp, times_dp, marker='s', linestyle='-', label='Dynamic Programming')
plt.xlabel('Size of n (number of segments)')
plt.ylabel('Runtime (seconds)')
plt.title('Runtime Comparison of Naive Recursive vs. Dynamic Programming')
plt.legend()
plt.grid(True)
plt.show()

