import heapq

def left(i):
    return 2*i + 1
    
def right(i):
    return 2*i + 2

def parent( i):
    return (i-1)//2
    

def heapify(A, i):
    if i < len(A):
        n = len(A)
        right_child_index = right(i)
        left_child_index = left(i)
        max_index = i

        if right_child_index < n and A[right_child_index] > A[max_index]:
            max_index = right_child_index
        if left_child_index < n and A[left_child_index] > A[max_index]:
            max_index = left_child_index

        if max_index != i:
            A[i], A[max_index] = A[max_index], A[i]  
            heapify(A, max_index)

def build_heap(array):
    n = len(array)
    for i in range(parent(n-1), -1, -1):
        heapify(array, i)


class MedianFinder:

    def __init__(self):
        self.lower_values = []
        self.higher_values = []

    def parent(self, i):
        return (i-1)//2

    def addNum(self, num: int) -> None:
        if len(self.lower_values) < len(self.higher_values):
            self.lower_values.append(-num)  
            i = len(self.lower_values) - 1   
            
            while i != 0 and self.lower_values.append[self.parent(i)] < self.lower_values.append[i]:
                self.lower_values.append[self.parent(i)], self.lower_values.append[i] = self.lower_values.append[i], self.lower_values.append[self.parent(i)]
                i = self.parent(i)            
        else:
            self.higher_values.append(-num)  
            i = len(self.lower_values) - 1   
            
            while i != 0 and self.higher_values.append[self.parent(i)] < self.higher_values.append[i]:
                self.higher_values.append[self.parent(i)], self.higher_values.append[i] = self.higher_values.append[i], self.higher_values.append[self.parent(i)]
                i = self.parent(i)    

    def findMedian(self) -> float:
        if self.lower_values == [] and self.higher_values == []:
            return None
        
        if len(self.lower_values > self.higher_values):
            return -self.lower_values[0]
        
        elif len(self.lower_values < self.higher_values):
            return -self.higher_values[0]
        
        else:
            return (-self.lower_values + (-self.higher_values)) / 2





def insert_into_heap(A, value):
    A.append(value)  # Step 1: Add the element to the end of the array
    i = len(A) - 1   # The index of the newly added element
    
    # Step 2: Perform up-heapification
    while i != 0 and A[parent(i)] < A[i]:
        A[parent(i)], A[i] = A[i], A[parent(i)]
        i = parent(i)

# Example usage:
arr2 = [10, 5, 3, 2, 4, 1, 7]
build_heap(arr2)
print("Heap before insertion:", arr2)

insert_into_heap(arr2, 15)
print("Heap after insertion:", arr2)




import heapq

class MedianFinder:

    def __init__(self):
        self.lower_values = []  # Max-Heap (simulated with negative values)
        self.higher_values = []  # Min-Heap

    def addNum(self, num: int) -> None:
        # Add new number to the max heap (lower_values)
        heapq.heappush(self.lower_values, -num)

        # Ensure the largest value in the lower_values is smaller than the smallest value in the higher_values
        if self.lower_values and self.higher_values and (-self.lower_values[0] > self.higher_values[0]):
            heapq.heappush(self.higher_values, -heapq.heappop(self.lower_values))

        # Balance the heaps if they have different sizes
        if len(self.lower_values) > len(self.higher_values) + 1:
            heapq.heappush(self.higher_values, -heapq.heappop(self.lower_values))
        if len(self.higher_values) > len(self.lower_values):
            heapq.heappush(self.lower_values, -heapq.heappop(self.higher_values))

    def findMedian(self) -> float:
        if len(self.lower_values) > len(self.higher_values):
            return -self.lower_values[0]
        elif len(self.higher_values) > len(self.lower_values):
            return self.higher_values[0]
        else:
            return (-self.lower_values[0] + self.higher_values[0]) / 2

