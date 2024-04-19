import sys


def T_dp(segment_lengths):
    n = 0
    for i in segment_lengths:
        n += 1
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

# def T_dp_with_traceback(segment_lengths):
#     n = 0
#     for i in segment_lengths:
#         n += 1
#     prefix_sum = [0]
#     dp = [[0] * n for _ in range(n)]
#     traceback = [[0] * n for _ in range(n)]
    
#     for i, length in enumerate(segment_lengths):
#         prefix_sum.append(prefix_sum[-1] + length)
#         dp[i][i] = length  
    
#     for length in range(2, n + 1):  
#         for i in range(n - length + 1):
#             j = i + length - 1
#             total_length = prefix_sum[j + 1] - prefix_sum[i]
#             left_choice = dp[i + 1][j]
#             right_choice = dp[i][j - 1]
#             if left_choice < right_choice:
#                 dp[i][j] = total_length - left_choice
#                 traceback[i][j] = 1
#             else:
#                 dp[i][j] = total_length - right_choice
#                 traceback[i][j] = -1
    
#     return dp[0][n - 1], traceback







def main(filename):
    with open(filename, 'r') as file:
        n = int(file.readline())
        segments = list(map(int, file.readline().split()))
        assert len(segments) == n, "Segment length doesn't match the n"
    max_length = T_dp(segments)
    print(max_length)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python main.py input.txt")
    else:
        main(sys.argv[1])
