class Solution:
    def twoSum(self, nums, target):
        # Create a hash map to store the complement and its index
        num_map = {}
        
        # Loop through the array
        for i, num in enumerate(nums):
            # Calculate the complement that we are looking for
            complement = target - num
            
            # If the complement is found in the hash map, return the indices
            if complement in num_map:
                return [num_map[complement], i]
            
            # Otherwise, add the current number and its index to the hash map
            num_map[num] = i