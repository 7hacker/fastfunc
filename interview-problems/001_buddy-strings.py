def buddy_strings(A, B):
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
                pairs.append((A[i]+B[i]))
            i = i+1
        if len(pairs) == 2:
            print(pairs)
            return pairs[0] == pairs[1][::-1]
    return False


def main():
    A = "xyyzabc"
    B = "xyzyabc"
    print(buddy_strings(A, B))


if __name__ == "__main__":
    main()
