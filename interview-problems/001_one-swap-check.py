'''
https://www.fastfunc.com/solution-intuition-one-swap-check/
'''


def one_swap_check(A, B):
    if len(A) != len(B):
        return False
    if A == B:
        seen = set()
        for char in A:
            if char in seen:
                return True
            seen.add(char)
        return False
    else:
        pairs = list()
        i = 0
        while i < len(A):
            if A[i] != B[i]:
                pairs.append((A[i], B[i]))
            i = i+1
        if len(pairs) == 2:
            return pairs[0][0] == pairs[1][1] and pairs[0][1] == pairs[1][0]
    return False


def main():
    A = "xyzp"
    B = "xzyp"
    print(one_swap_check(A, B))


if __name__ == "__main__":
    main()
