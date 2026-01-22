class Solution(object):
    def minimumPairRemoval(self, nums):
        arr = nums[:] 
        operations = 0
        
        while True:
            is_sorted = True
            for i in range(len(arr) - 1):
                if arr[i] > arr[i+1]:
                    is_sorted = False
                    break
            
            if is_sorted:
                return operations

            min_sum = float('inf')
            idx = -1
            
            for i in range(len(arr) - 1):
                current_sum = arr[i] + arr[i+1]
                if current_sum < min_sum:
                    min_sum = current_sum
                    idx = i
    
            new_val = arr[idx] + arr[idx+1]
            arr[idx] = new_val
            arr.pop(idx + 1)
            
            operations += 1