def equal(A, B):
    # O(N)
    if len(A) != len(B):
        return False
    for i in range(len(A)):
        if A[i] != B[i]:
            return False
    return True


def search_substring(s, sub):
    # O(N*M)
    for i in range(0,len(s)-len(sub)):
        if equal(s[i:i+len(sub)], sub):
            print(i)