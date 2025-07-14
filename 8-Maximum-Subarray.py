"""
Problem: Maximum Subarray (Kadane's Algorithm)
Difficulty: Easy
Category: Arrays & Strings

Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Time Complexity Analysis:
- Solution 1 (Kadane's Algorithm): O(n) time, O(1) space
- Solution 2 (Divide and Conquer): O(n log n) time, O(log n) space
- Solution 3 (Brute Force): O(n²) time, O(1) space
"""

def max_subarray_kadane(nums):
    """
    Solution 1: Kadane's Algorithm (Most Efficient)
    Time Complexity: O(n) - We traverse the array once
    Space Complexity: O(1) - We only use a constant amount of extra space
    
    Algorithm:
    1. Keep track of current sum and maximum sum
    2. For each element, add to current sum
    3. If current sum becomes negative, reset to 0
    4. Update maximum sum if current sum is greater
    5. This is the most efficient approach
    """
    # Handle empty array
    if not nums:
        return 0
    
    # Initialize variables
    current_sum = nums[0]  # Start with first element
    max_sum = nums[0]  # Initialize max sum with first element
    
    # Traverse array starting from second element
    for i in range(1, len(nums)):
        # Add current element to current sum
        current_sum += nums[i]
        
        # If current element is greater than current sum, start fresh
        if nums[i] > current_sum:
            current_sum = nums[i]
        
        # Update maximum sum if current sum is greater
        if current_sum > max_sum:
            max_sum = current_sum
    
    return max_sum


def max_subarray_divide_conquer(nums):
    """
    Solution 2: Divide and Conquer Approach
    Time Complexity: O(n log n) - We divide the problem in half each time
    Space Complexity: O(log n) - Due to recursion call stack
    
    Algorithm:
    1. Divide array into two halves
    2. Recursively find max subarray in left and right halves
    3. Find max subarray crossing the middle
    4. Return maximum of three values
    5. This demonstrates divide and conquer thinking
    """
    def max_crossing_subarray(nums, low, mid, high):
        """Find maximum subarray crossing the middle"""
        # Find maximum sum in left half
        left_sum = float('-inf')
        current_sum = 0
        for i in range(mid, low - 1, -1):
            current_sum += nums[i]
            left_sum = max(left_sum, current_sum)
        
        # Find maximum sum in right half
        right_sum = float('-inf')
        current_sum = 0
        for i in range(mid + 1, high + 1):
            current_sum += nums[i]
            right_sum = max(right_sum, current_sum)
        
        return left_sum + right_sum
    
    def max_subarray_helper(nums, low, high):
        """Recursive helper function"""
        # Base case: single element
        if low == high:
            return nums[low]
        
        # Find middle point
        mid = (low + high) // 2
        
        # Recursively find maximum subarray in left and right halves
        left_max = max_subarray_helper(nums, low, mid)
        right_max = max_subarray_helper(nums, mid + 1, high)
        
        # Find maximum subarray crossing the middle
        cross_max = max_crossing_subarray(nums, low, mid, high)
        
        # Return maximum of three values
        return max(left_max, right_max, cross_max)
    
    # Handle empty array
    if not nums:
        return 0
    
    return max_subarray_helper(nums, 0, len(nums) - 1)


def max_subarray_brute_force(nums):
    """
    Solution 3: Brute Force Approach
    Time Complexity: O(n²) - We check every possible subarray
    Space Complexity: O(1) - Only using a constant amount of extra space
    
    Algorithm:
    1. Use two nested loops to generate all possible subarrays
    2. Calculate sum of each subarray
    3. Keep track of maximum sum found
    4. This is the most straightforward but least efficient approach
    """
    # Handle empty array
    if not nums:
        return 0
    
    n = len(nums)
    max_sum = float('-inf')  # Initialize with negative infinity
    
    # Generate all possible subarrays
    for i in range(n):  # Start index
        current_sum = 0
        for j in range(i, n):  # End index
            current_sum += nums[j]  # Add current element
            max_sum = max(max_sum, current_sum)  # Update maximum
    
    return max_sum


def max_subarray_dp(nums):
    """
    Solution 4: Dynamic Programming Approach
    Time Complexity: O(n) - We traverse the array once
    Space Complexity: O(n) - We use a DP array
    
    Algorithm:
    1. Use DP array where dp[i] represents max sum ending at index i
    2. dp[i] = max(nums[i], dp[i-1] + nums[i])
    3. Return maximum value in DP array
    4. This demonstrates dynamic programming thinking
    """
    # Handle empty array
    if not nums:
        return 0
    
    n = len(nums)
    dp = [0] * n  # DP array
    dp[0] = nums[0]  # Base case
    
    # Fill DP array
    for i in range(1, n):
        # Either start fresh with current element or extend previous subarray
        dp[i] = max(nums[i], dp[i - 1] + nums[i])
    
    # Return maximum value in DP array
    return max(dp)


# Test cases to demonstrate all solutions
def test_max_subarray():
    """Test function to demonstrate all solutions"""
    
    test_cases = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],  # Standard case
        [1],  # Single element
        [-1],  # Single negative element
        [-2, -1],  # All negative
        [1, 2, 3, 4],  # All positive
        [],  # Empty array
        [0, 0, 0],  # All zeros
        [-1, -2, -3, -4],  # All negative
        [5, 4, -1, 7, 8],  # Another case
    ]
    
    print("=== Maximum Subarray Test Cases ===")
    for i, test_case in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        print(f"Array: {test_case}")
        
        # Test all solutions
        result1 = max_subarray_kadane(test_case.copy())
        result2 = max_subarray_divide_conquer(test_case.copy())
        result3 = max_subarray_brute_force(test_case.copy())
        result4 = max_subarray_dp(test_case.copy())
        
        print(f"Kadane's: {result1}")
        print(f"Divide & Conquer: {result2}")
        print(f"Brute Force: {result3}")
        print(f"Dynamic Programming: {result4}")
        
        # Check if all solutions agree
        all_same = all([result1 == result2, result2 == result3, result3 == result4])
        print(f"All solutions agree: {all_same}")


# Main execution
if __name__ == "__main__":
    print("=== Maximum Subarray Problem - 4 Solutions ===")
    print("1. Kadane's Algorithm (O(n) time, O(1) space) - RECOMMENDED")
    print("2. Divide & Conquer (O(n log n) time, O(log n) space)")
    print("3. Brute Force (O(n²) time, O(1) space)")
    print("4. Dynamic Programming (O(n) time, O(n) space)")
    print()
    
    # Run test cases
    test_max_subarray()
    
    print("\n=== Summary ===")
    print("• Kadane's Algorithm is most efficient")
    print("• Divide & Conquer shows recursive thinking")
    print("• Brute Force is simple but inefficient")
    print("• Dynamic Programming demonstrates DP concepts")
    print("• All solutions handle edge cases properly")