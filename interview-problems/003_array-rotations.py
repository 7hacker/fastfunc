'''
https://www.fastfunc.com/array-rotations/
'''


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


def rotate_array(A, k, right=True):
    '''
    Rotate elements in A by k positions.
    Right rotate by default
    '''
    A = reverse(A, 0, len(A)-1)
    if right:
        A = reverse(A, 0, k-1)
        A = reverse(A, k, len(A)-1)
    else:
        A = reverse(A, 0, len(A)-k-1)
        A = reverse(A, len(A)-k, len(A)-1)
    return A


def main():
    A = [1, 2, 3, 4, 5, 6]
    k = 2
    print(A)
    A = rotate_array(A, k)
    print(A)


if __name__ == "__main__":
    main()
