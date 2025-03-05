import heapq

heap = []

heapq.heappush(heap, 31)
heapq.heappush(heap, 13)
heapq.heappush(heap, 3)
heapq.heappush(heap, 23)
heapq.heappush(heap, 34)

while heap:
    val = heapq.heappop(heap)
    print(val)