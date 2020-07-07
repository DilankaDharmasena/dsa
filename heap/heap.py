'''
Time Complexity:
    peek: O(1)
    pop: O(log n)
    push: O(log n)
    init: ~O(n)
'''

import math

class Heap:

    def __init__(self, initial_values=[]):
        len_initial_values = len(initial_values)
        self.capacity = 10 if len_initial_values < 5 else len_initial_values * 2
        self.size = len_initial_values
        self.heap_array = list(initial_values)
        self.heap_array.extend([0] * (self.capacity - self.size))
        for i in range((self.size - 1)//2, -1, -1): # Running it on leaves is pointless
            self.__heapify_down(i)

    def __str__(self):
        return str(self.heap_array)

    def __get_left_child_index(self, parent_index):
        return (parent_index * 2) + 1

    def __get_right_child_index(self, parent_index):
        return (parent_index * 2) + 2

    def __get_parent_index(self, child_index):
        return (child_index - 1) // 2
    
    def __left_child_exists(self, parent_index):
        if self.__get_left_child_index(parent_index) < self.size:
            return True
        else:
            return False

    def __right_child_exists(self, parent_index):
        if self.__get_right_child_index(parent_index) < self.size:
            return True
        else:
            return False

    def __parent_exists(self, child_index):
        if child_index > 0:
            return True
        else:
            return False

    def __get_left_child(self, parent_index):
        if self.__left_child_exists(parent_index):
            return self.heap_array[self.__get_left_child_index(parent_index)]
        else:
            return None
    
    def __get_right_child(self, parent_index):
        if self.__right_child_exists(parent_index):
            return self.heap_array[self.__get_right_child_index(parent_index)]
        else:
            return None

    def __get_parent(self, child_index):
        if self.__parent_exists(child_index):
            return self.heap_array[self.__get_parent_index(child_index)]
        else:
            return None

    def __get_smallest_index(self, index):
        current_val = (self.heap_array[index], index)
        left_child_val = (self.__get_left_child(index), self.__get_left_child_index(index))
        right_child_val = (self.__get_right_child(index), self.__get_right_child_index(index))
        min_val = min((i for i in [current_val, left_child_val, right_child_val] if i[0] is not None), key = lambda k: k[0])
        return min_val[1]

    def __swap(self, index_1, index_2):
        temp_val = self.heap_array[index_1]
        self.heap_array[index_1] = self.heap_array[index_2]
        self.heap_array[index_2] = temp_val

    def __check_capacity(self):
        if self.size == self.capacity:
            self.heap_array.extend([0] * len(self.heap_array))
            self.capacity = len(self.heap_array)

    def __heapify_down(self, index):
        while self.__left_child_exists(index) or self.__right_child_exists(index):
            min_index = self.__get_smallest_index(index)
            if min_index == index:
                break
            else:
                self.__swap(index, min_index)
                index = min_index

    def __heapify_up(self, index):
        parent_val = self.__get_parent(index)
        while parent_val is not None:
            if self.heap_array[index] < parent_val:
                parent_index = self.__get_parent_index(index)
                self.__swap(index, parent_index)
                index = parent_index
                parent_val = self.__get_parent(parent_index)
            else:
                break

    def peek(self):
        if self.size == 0:
            return None
        else:
            return self.heap_array[0]

    def pop(self):
        if self.size == 0:
            return None
        else:
            retVal = self.heap_array[0]
            self.size -= 1
            if self.size > 0:
                self.__swap(0, self.size)
                self.__heapify_down(0)
            return retVal

    def push(self, value):
        self.__check_capacity()
        self.heap_array[self.size] = value
        self.size += 1
        self.__heapify_up(self.size - 1)

    def __num_nodes_at_level(self, level):
        return math.pow(2, level)

    def __get_nodes_at_level(self, level):
        offset = 0
        # Add memo to bring print_heap to O(n)
        for i in range(0, level):
            offset += self.__num_nodes_at_level(i)
        
        end = offset + self.__num_nodes_at_level(level)
        end = self.size if end > self.size else end

        return self.heap_array[int(offset):int(end)]

    def __calculate_print_buffer_length(self, height, level, longest_node_val):
        num_sections = int(math.pow(2, height - level)) - 1
        return num_sections * longest_node_val

    def print_heap(self):
        longest_node_val = 0
        for i in self.heap_array:
            longest_node_val = max(longest_node_val, len(str(i)))

        height = -1 if self.size == 0 else math.log2(self.size)
        height = math.floor(height)
        for i in range(0, height + 1):
            print_buffer_length = self.__calculate_print_buffer_length(height, i, longest_node_val)
            print_buffer = " " * print_buffer_length
            nodes = self.__get_nodes_at_level(i)
            for j in nodes:
                print(print_buffer, str(j).ljust(longest_node_val), print_buffer, end=(" " * longest_node_val), sep="")
            print("")
