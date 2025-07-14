"""
Problem: Missing Number
Difficulty: Easy
Category: Arrays & Strings

Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.

Example:
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 
2 is the missing number in the range since it does not appear in nums.

Time Complexity Analysis:
- Solution 1 (Sum): O(n) time, O(1) space
- Solution 2 (XOR): O(n) time, O(1) space
- Solution 3 (Sort): O(n log n) time, O(1) space
"""

def missing_number_sum(nums):
    """
    Solution 1: Sum Approach (Most Efficient)
    Time Complexity: O(n) - We traverse the array once
    Space Complexity: O(1) - We only use a constant amount of extra space
    
    Algorithm:
    1. Calculate expected sum: n * (n + 1) / 2
    2. Calculate actual sum of array
    3. Difference is the missing number
    4. This is the most efficient approach
    """
    n = len(nums)  # Length of array
    expected_sum = n * (n + 1) // 2  # Sum of 0 to n
    actual_sum = sum(nums)  # Sum of array
    
    return expected_sum - actual_sum


def missing_number_xor(nums):
    """
    Solution 2: XOR Approach
    Time Complexity: O(n) - We traverse the array once
    Space Complexity: O(1) - We only use a constant amount of extra space
    
    Algorithm:
    1. XOR all numbers from 0 to n
    2. XOR all numbers in array
    3. Result is the missing number
    4. This uses bit manipulation
    """
    result = len(nums)  # Start with n
    
    # XOR with all numbers from 0 to n-1 and array elements
    for i in range(len(nums)):
        result ^= i ^ nums[i]
    
    return result


def missing_number_sort(nums):
    """
    Solution 3: Sorting Approach
    Time Complexity: O(n log n) - Due to sorting
    Space Complexity: O(1) - In-place sorting
    
    Algorithm:
    1. Sort the array
    2. Check if each number is at correct index
    3. Return the missing number
    4. This is less efficient but straightforward
    """
    nums.sort()  # Sort the array
    
    # Check each position
    for i in range(len(nums)):
        if nums[i] != i:
            return i
    
    # If all positions are correct, missing number is n
    return len(nums)


# Test cases to demonstrate all solutions
def test_missing_number():
    """Test function to demonstrate all solutions"""
    
    test_cases = [
        [3, 0, 1],
        [0, 1],
        [9, 6, 4, 2, 3, 5, 7, 0, 1],
        [0],
        [1],
    ]
    
    print("=== Missing Number Test Cases ===")
    for i, test_case in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        print(f"Input: {test_case}")
        
        # Test all solutions
        result1 = missing_number_sum(test_case.copy())
        result2 = missing_number_xor(test_case.copy())
        result3 = missing_number_sort(test_case.copy())
        
        print(f"Sum: {result1}")
        print(f"XOR: {result2}")
        print(f"Sort: {result3}")
        
        # Check if all solutions agree
        all_same = all([result1 == result2, result2 == result3])
        print(f"All solutions agree: {all_same}")


# Main execution
if __name__ == "__main__":
    print("=== Missing Number Problem - 3 Solutions ===")
    print("1. Sum (O(n) time, O(1) space) - RECOMMENDED")
    print("2. XOR (O(n) time, O(1) space)")
    print("3. Sort (O(n log n) time, O(1) space)")
    print()
    
    # Run test cases
    test_missing_number()
    
    print("\n=== Summary ===")
    print("• Sum approach is most efficient")
    print("• XOR approach uses bit manipulation")
    print("• Sort approach is straightforward but slower")
    print("• All solutions handle edge cases properly")