import numpy as np
import timeit

# Assuming we have the dynamic programming function T_dp available
# Let's define a simplified version of T_dp for demonstration
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

# Re-generate the runtime data for the dynamic programming approach
n_values_dp = np.array(range(10, 201, 10))
times_dp = []

for n in n_values_dp:
    np.random.seed(42)  # for reproducibility
    segments = np.random.randint(1, 1000, n)
    start_time = timeit.default_timer()
    T_dp(segments)
    times_dp.append(timeit.default_timer() - start_time)

# Perform quadratic regression
coefficients = np.polyfit(n_values_dp, times_dp, 2)  # 2 indicates a quadratic fit
equation = np.poly1d(coefficients)
print("Quadratic regression equation:")
print(equation)