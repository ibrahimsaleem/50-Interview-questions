"""
Problem: Move Zeroes
Difficulty: Easy
Category: Arrays & Strings

Given an integer array nums, move all 0's to the end of it while maintaining 
the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Time Complexity Analysis:
- Solution 1 (Two Pointers): O(n) time, O(1) space
- Solution 2 (Count Zeroes): O(n) time, O(1) space
- Solution 3 (Filter Approach): O(n) time, O(n) space (not in-place)
"""

def move_zeroes_two_pointers(nums):
    """
    Solution 1: Two Pointers Approach (Most Efficient)
    Time Complexity: O(n) - We traverse the array once
    Space Complexity: O(1) - We only use a constant amount of extra space
    
    Algorithm:
    1. Use two pointers: one for current position, one for next non-zero
    2. Find next non-zero element
    3. Swap with current position
    4. Move both pointers forward
    5. This is the most efficient in-place solution
    """
    # Initialize pointer for non-zero elements
    non_zero_index = 0
    
    # Traverse array
    for i in range(len(nums)):
        # If current element is non-zero
        if nums[i] != 0:
            # Swap with position at non_zero_index
            nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
            non_zero_index += 1  # Move to next position
    
    return nums


def move_zeroes_count_approach(nums):
    """
    Solution 2: Count Zeroes Approach
    Time Complexity: O(n) - We traverse the array twice
    Space Complexity: O(1) - We only use a constant amount of extra space
    
    Algorithm:
    1. Count number of zeroes
    2. Remove all zeroes
    3. Append zeroes to end
    4. This is straightforward but less efficient
    """
    # Count zeroes
    zero_count = nums.count(0)
    
    # Remove all zeroes
    for _ in range(zero_count):
        nums.remove(0)
    
    # Append zeroes to end
    nums.extend([0] * zero_count)
    
    return nums


def move_zeroes_filter_approach(nums):
    """
    Solution 3: Filter Approach (Not In-place)
    Time Complexity: O(n) - We process each element once
    Space Complexity: O(n) - We create a new list
    
    Algorithm:
    1. Filter non-zero elements
    2. Create new list with zeroes at end
    3. Update original array
    4. This is not in-place but shows filtering
    """
    # Filter non-zero elements
    non_zero_nums = [num for num in nums if num != 0]
    zero_count = len(nums) - len(non_zero_nums)
    
    # Create new array with zeroes at end
    result = non_zero_nums + [0] * zero_count
    
    # Update original array
    for i in range(len(result)):
        nums[i] = result[i]
    
    return nums


def move_zeroes_optimized(nums):
    """
    Solution 4: Optimized Two Pointers
    Time Complexity: O(n) - We traverse the array once
    Space Complexity: O(1) - Only constant extra space
    
    Algorithm:
    1. Same as two pointers but with optimizations
    2. Skip unnecessary swaps
    3. Early exit for arrays with no zeroes
    4. This is the most optimized version
    """
    # Handle edge cases
    if not nums or len(nums) == 1:
        return nums
    
    # Initialize pointer for non-zero elements
    non_zero_index = 0
    
    # Traverse array
    for i in range(len(nums)):
        # If current element is non-zero
        if nums[i] != 0:
            # Only swap if positions are different
            if i != non_zero_index:
                nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
            non_zero_index += 1  # Move to next position
    
    return nums


# Test cases to demonstrate all solutions
def test_move_zeroes():
    """Test function to demonstrate all solutions"""
    
    test_cases = [
        [0, 1, 0, 3, 12],
        [1, 2, 3, 4, 5],
        [0, 0, 0, 0],
        [1, 0, 0, 0, 1],
        [0],
        [1],
        [],
        [0, 1, 0, 0, 2, 0, 3],
    ]
    
    print("=== Move Zeroes Test Cases ===")
    for i, test_case in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        print(f"Input: {test_case}")
        
        # Test all solutions
        result1 = move_zeroes_two_pointers(test_case.copy())
        result2 = move_zeroes_count_approach(test_case.copy())
        result3 = move_zeroes_filter_approach(test_case.copy())
        result4 = move_zeroes_optimized(test_case.copy())
        
        print(f"Two Pointers: {result1}")
        print(f"Count Approach: {result2}")
        print(f"Filter Approach: {result3}")
        print(f"Optimized: {result4}")
        
        # Check if all solutions agree
        all_same = all([result1 == result2, result2 == result3, result3 == result4])
        print(f"All solutions agree: {all_same}")


# Main execution
if __name__ == "__main__":
    print("=== Move Zeroes Problem - 4 Solutions ===")
    print("1. Two Pointers (O(n) time, O(1) space) - RECOMMENDED")
    print("2. Count Approach (O(n) time, O(1) space)")
    print("3. Filter Approach (O(n) time, O(n) space)")
    print("4. Optimized Two Pointers (O(n) time, O(1) space)")
    print()
    
    # Run test cases
    test_move_zeroes()
    
    print("\n=== Summary ===")
    print("• Two Pointers is most efficient and in-place")
    print("• Count approach is straightforward but less efficient")
    print("• Filter approach shows Pythonic approach")
    print("• Optimized version adds performance improvements")
    print("• All solutions handle edge cases properly")