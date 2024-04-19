def T_dp_with_traceback(segment_lengths):
    n = len(segment_lengths)
    prefix_sum = [0]
    dp = [[(0, '') for _ in range(n)] for _ in range(n)]  
    
    # Initialize prefix sum and diagonal of DP table
    for i, length in enumerate(segment_lengths):
        prefix_sum.append(prefix_sum[-1] + length)
        dp[i][i] = (length, '')  # No direction on single segments

    # Fill the DP table
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            total_length = prefix_sum[j + 1] - prefix_sum[i]

            # Calculate values from left and right
            left_value = total_length - dp[i + 1][j][0]
            right_value = total_length - dp[i][j - 1][0]

            # Tie-breaking rule: prefer the left segment if equal
            if left_value >= right_value:
                dp[i][j] = (left_value, 'L')
            else:
                dp[i][j] = (right_value, 'R')
    
    # Traceback to find the sequence of picks
    sequence = []
    i, j = 0, n - 1
    while i != j:
        if dp[i][j][1] == 'L':
            sequence.append(i + 1)
            i += 1
        else:
            sequence.append(j + 1)
            j -= 1
    sequence.append(i + 1)  # add the last segment

    max_length = dp[0][n - 1][0]
    return max_length, sequence

    



def main(filename):
    with open(filename, 'r') as file:
        n = int(file.readline().strip())
        segments = list(map(int, file.readline().strip().split()))
        assert len(segments) == n, "Segment length doesn't match the number of segments"
    
    max_length, sequence = T_dp_with_traceback(segments)
    print(max_length)
    print(' '.join(map(str, sequence)))

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python main.py input.txt")
    else:
        main(sys.argv[1])
