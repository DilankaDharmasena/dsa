from heap import Heap

initial_values = list(range(50, -1, -1)) # Worst case ordering of initial values

minHeap = Heap(initial_values)
minHeap.print_heap()

minHeap.push(-1)
minHeap.print_heap()

minHeap.pop()
minHeap.print_heap()
