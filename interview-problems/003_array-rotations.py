
def reverse(A, start, end):
    # reverse elements in A from start index to end index, inclusive
    if end >= len(A):
        pass
    else:
        while start < end:
            temp = A[end]
            A[end] = A[start]
            A[start] = temp
            start = start + 1
            end = end - 1
    return A


def right_rotate_array(A, k):
    '''
    Right Rotate elements in A by k positions.
    '''
    # downsize k
    k = k % len(A)

    # First reversal
    A = reverse(A, 0, len(A)-1)

    # Second Reversal
    A = reverse(A, 0, k-1)
    A = reverse(A, k, len(A)-1)

    return A


def main():
    A = [1, 2, 3, 4, 5, 6]
    k = 2
    print(A)
    A = right_rotate_array(A, k)
    print(A)


if __name__ == "__main__":
    main()
