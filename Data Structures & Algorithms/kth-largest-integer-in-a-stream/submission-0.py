class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k 
        for num in nums:
            self.add(num)


    def add(self, val: int) -> int:
        self.heap.append(val)
        curr = len(self.heap) - 1

        while curr > 0 and self.heap[curr] < self.heap[(curr - 1) // 2]:
            self.heap[curr], self.heap[(curr - 1) // 2] = self.heap[(curr - 1) // 2], self.heap[curr]
            curr = (curr - 1) // 2
        
        if len(self.heap) > self.k:
            self.remove()
        
        return self.heap[0]
    
    def remove(self):
        if len(self.heap) == 0:
            return None 
        if len(self.heap) == 1:
            return self.heap.pop() 
        
        max_heap = self.heap[0]
        self.heap[0] = self.heap.pop() 
        self.sink_down(0)

        return max_heap

    def sink_down(self, index):
        max_index = index 

        while True:

            left = 2 * index + 1
            right = 2 * index + 2 

            if left < len(self.heap) and self.heap[left] < self.heap[max_index]:
                max_index = left 
            if right < len(self.heap) and self.heap[right] < self.heap[max_index]:
                max_index = right 
            if max_index != index:
                self.heap[max_index], self.heap[index] = self.heap[index], self.heap[max_index]
                index = max_index
            else:
                return 
        

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)