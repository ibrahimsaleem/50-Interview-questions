"""
Problem: Two Sum
Difficulty: Easy
Category: Arrays & Strings

Given an array of integers nums and an integer target, return indices of the two numbers 
such that they add up to target. You may assume that each input would have exactly one 
solution, and you may not use the same element twice.

Example:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Time Complexity Analysis:
- Solution 1 (Brute Force): O(n²) time, O(1) space
- Solution 2 (Hash Map): O(n) time, O(n) space  
- Solution 3 (Two Pointers): O(n log n) time, O(1) space (requires sorted array)
"""

def two_sum_brute_force(nums, target):
    """
    Solution 1: Brute Force Approach
    Time Complexity: O(n²) - We check every pair of numbers
    Space Complexity: O(1) - Only using a constant amount of extra space
    
    Algorithm:
    1. Use two nested loops to check every possible pair
    2. If sum equals target, return the indices
    3. This is the most straightforward but least efficient approach
    """
    n = len(nums)  # Get the length of the array
    
    # Outer loop: iterate through each element as the first number
    for i in range(n):
        # Inner loop: iterate through remaining elements as the second number
        for j in range(i + 1, n):  # Start from i+1 to avoid using same element twice
            # Check if current pair sums to target
            if nums[i] + nums[j] == target:
                return [i, j]  # Return indices when found
    
    return []  # Return empty list if no solution found


def two_sum_hash_map(nums, target):
    """
    Solution 2: Hash Map Approach (Most Efficient)
    Time Complexity: O(n) - We only need to traverse the array once
    Space Complexity: O(n) - We store up to n elements in the hash map
    
    Algorithm:
    1. Use a hash map to store numbers we've seen and their indices
    2. For each number, check if (target - current_number) exists in hash map
    3. If found, we have our pair; if not, add current number to hash map
    4. This is the most efficient approach for this problem
    """
    # Create a hash map to store numbers and their indices
    num_map = {}  # Key: number, Value: index
    
    # Iterate through the array once
    for i, num in enumerate(nums):
        # Calculate the complement (what we need to add to current number to get target)
        complement = target - num
        
        # Check if complement exists in our hash map
        if complement in num_map:
            # Found the pair! Return both indices
            return [num_map[complement], i]
        
        # If complement not found, add current number and its index to hash map
        num_map[num] = i
    
    return []  # Return empty list if no solution found


def two_sum_two_pointers(nums, target):
    """
    Solution 3: Two Pointers Approach (Requires Sorted Array)
    Time Complexity: O(n log n) - Due to sorting, then O(n) for two pointers
    Space Complexity: O(1) - Only using a constant amount of extra space
    
    Note: This approach requires the array to be sorted, which changes the original problem
    slightly. We'll create a sorted copy with original indices.
    
    Algorithm:
    1. Create a list of tuples (value, original_index) and sort by value
    2. Use two pointers: one at start, one at end
    3. If sum < target, move left pointer right; if sum > target, move right pointer left
    4. Continue until we find the pair or pointers meet
    """
    # Create list of tuples with original indices
    nums_with_indices = [(nums[i], i) for i in range(len(nums))]
    
    # Sort by the values (first element of each tuple)
    nums_with_indices.sort(key=lambda x: x[0])
    
    # Initialize two pointers
    left = 0  # Start from beginning
    right = len(nums_with_indices) - 1  # Start from end
    
    # Continue while pointers haven't met
    while left < right:
        # Calculate current sum
        current_sum = nums_with_indices[left][0] + nums_with_indices[right][0]
        
        # If we found the target sum
        if current_sum == target:
            # Return original indices (second element of tuples)
            return [nums_with_indices[left][1], nums_with_indices[right][1]]
        
        # If sum is less than target, move left pointer right (to increase sum)
        elif current_sum < target:
            left += 1
        
        # If sum is greater than target, move right pointer left (to decrease sum)
        else:
            right -= 1
    
    return []  # Return empty list if no solution found


# Test cases to demonstrate all three solutions
def test_two_sum():
    """Test function to demonstrate all three solutions"""
    
    # Test case 1: Basic case
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print("Test Case 1:")
    print(f"Array: {nums1}, Target: {target1}")
    print(f"Expected: [0, 1]")
    print(f"Brute Force: {two_sum_brute_force(nums1, target1)}")
    print(f"Hash Map: {two_sum_hash_map(nums1, target1)}")
    print(f"Two Pointers: {two_sum_two_pointers(nums1, target1)}")
    print()
    
    # Test case 2: Numbers at the end
    nums2 = [3, 2, 4]
    target2 = 6
    print("Test Case 2:")
    print(f"Array: {nums2}, Target: {target2}")
    print(f"Expected: [1, 2]")
    print(f"Brute Force: {two_sum_brute_force(nums2, target2)}")
    print(f"Hash Map: {two_sum_hash_map(nums2, target2)}")
    print(f"Two Pointers: {two_sum_two_pointers(nums2, target2)}")
    print()
    
    # Test case 3: Same numbers
    nums3 = [3, 3]
    target3 = 6
    print("Test Case 3:")
    print(f"Array: {nums3}, Target: {target3}")
    print(f"Expected: [0, 1]")
    print(f"Brute Force: {two_sum_brute_force(nums3, target3)}")
    print(f"Hash Map: {two_sum_hash_map(nums3, target3)}")
    print(f"Two Pointers: {two_sum_two_pointers(nums3, target3)}")
    print()


# Interactive demo
def interactive_demo():
    """Interactive demo where user can input their own test cases"""
    print("=== Two Sum Problem - Interactive Demo ===")
    print("Enter array elements separated by spaces (e.g., 2 7 11 15):")
    
    try:
        # Get array input from user
        nums_input = input("Array: ").strip()
        nums = [int(x) for x in nums_input.split()]
        
        # Get target from user
        target = int(input("Target: "))
        
        print(f"\nResults for array {nums} with target {target}:")
        print(f"Brute Force: {two_sum_brute_force(nums, target)}")
        print(f"Hash Map: {two_sum_hash_map(nums, target)}")
        print(f"Two Pointers: {two_sum_two_pointers(nums, target)}")
        
    except ValueError:
        print("Invalid input! Please enter valid integers.")


# Main execution
if __name__ == "__main__":
    print("=== Two Sum Problem - 3 Solutions ===")
    print("1. Brute Force (O(n²) time, O(1) space)")
    print("2. Hash Map (O(n) time, O(n) space) - RECOMMENDED")
    print("3. Two Pointers (O(n log n) time, O(1) space)")
    print()
    
    # Run test cases
    test_two_sum()
    
    # Ask if user wants interactive demo
    choice = input("Would you like to try your own test case? (y/n): ").lower()
    if choice == 'y':
        interactive_demo()
    
    print("\n=== Summary ===")
    print("• Hash Map solution is the most efficient for this problem")
    print("• Brute Force is simple but inefficient")
    print("• Two Pointers requires sorting but uses minimal space")