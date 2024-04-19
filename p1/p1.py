import sys

def T(segment_lengths, i, j):
    if i == j:
        return segment_lengths[i]
    
    total_length = 0
    for k in range(i, j + 1):
        total_length += segment_lengths[k]
    
    left_choice = T(segment_lengths, i + 1, j)
    right_choice = T(segment_lengths, i, j - 1)

    min_value = left_choice if left_choice < right_choice else right_choice

    return total_length - min_value


def main(filename):
    with open(filename, 'r') as file:
        n = int(file.readline())
        segments = list(map(int, file.readline().split()))
        assert len(segments) == n, "Segment length doesn't match the n"
    max_length = T(segments, 0, n - 1)
    print(max_length)


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python timber_problem.py input.txt")
    else:
        main(sys.argv[1])
