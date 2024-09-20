def three_sum(nums):
    # Sort the array to facilitate finding triplets
    nums.sort()
    triplets = []
    
    for i in range(len(nums) - 2):
        # Skip duplicate values for the first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum < 0:
                left += 1  # Need a larger sum
            elif current_sum > 0:
                right -= 1  # Need a smaller sum
            else:
                # Found a triplet
                triplets.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates for the second element
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicates for the third element
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1

    return triplets

# Example usage
if __name__ == "__main__":
    array = [-1, 0, 1, 2, -1, -4]
    result = three_sum(array)
    print("Triplets that sum to zero:", result)
