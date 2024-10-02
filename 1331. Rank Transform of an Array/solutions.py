class Solution:
    def arrayRankTransform(self, arr):
        # Check if the input array is empty, return an empty list if true
        if not arr:
            return []
        
        # Create a sorted copy of the original array to determine ranks
        sorted_arr = sorted(set(arr))  # Removing duplicates and sorting
        
        # Create a dictionary to store the rank of each unique element
        rank_map = {val: rank + 1 for rank, val in enumerate(sorted_arr)}
        
        # Create a result list and replace each element in the original array with its rank
        result = [rank_map[num] for num in arr]
        
        # Return the result list containing ranks
        return result
