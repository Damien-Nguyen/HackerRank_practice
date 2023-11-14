#QHEAP1
# Enter your code here. Read input from STDIN. Print output to STDOUT
from heapq import heappush, heappop

#initialize the variables
heap = []
lookup = set()

for i in range(int(input())):
    t = list(map(int, input().split()))
    
    # process the queries
    # insertion 
    if t[0] == 1:
        heappush(heap, t[1])
        lookup.add(t[1])
    # deletion
    elif t[0] == 2:
        lookup.discard(t[1])
    # print the minimum element
    else:
        # delete the min element until it's in lookup set
        while heap[0] not in lookup:
            heappop(heap)
        
        print(heap[0])