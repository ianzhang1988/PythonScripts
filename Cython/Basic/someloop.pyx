cpdef int cloop(int n):
    cdef int sum = 0
    cdef int i
    for i in range(1, n+1):
        sum+=i
    return sum