"""
Problem: Single Number
Difficulty: Easy
Category: Arrays & Strings

Given a non-empty array of integers nums, every element appears twice except for one. 
Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example:
Input: nums = [2,2,1]
Output: 1

Time Complexity Analysis:
- Solution 1 (XOR): O(n) time, O(1) space
- Solution 2 (Hash Set): O(n) time, O(n) space
- Solution 3 (Math): O(n) time, O(n) space
"""

def single_number_xor(nums):
    """
    Solution 1: XOR Approach (Most Efficient)
    Time Complexity: O(n) - We traverse the array once
    Space Complexity: O(1) - We only use a constant amount of extra space
    
    Algorithm:
    1. Use XOR operation: a ^ a = 0, a ^ 0 = a
    2. XOR all elements together
    3. Result is the single number
    4. This is the most efficient approach
    """
    result = 0  # Initialize result
    
    # XOR all elements
    for num in nums:
        result ^= num
    
    return result


def single_number_hash_set(nums):
    """
    Solution 2: Hash Set Approach
    Time Complexity: O(n) - We traverse the array once
    Space Complexity: O(n) - We use a hash set
    
    Algorithm:
    1. Use hash set to track seen numbers
    2. Add numbers to set, remove if already present
    3. Remaining number is the single one
    4. This is straightforward but uses extra space
    """
    seen = set()  # Hash set to track seen numbers
    
    # Traverse array
    for num in nums:
        if num in seen:
            seen.remove(num)  # Remove if already seen
        else:
            seen.add(num)  # Add if not seen
    
    # Return the single number
    return seen.pop()


def single_number_math(nums):
    """
    Solution 3: Mathematical Approach
    Time Complexity: O(n) - We traverse the array once
    Space Complexity: O(n) - We use a set
    
    Algorithm:
    1. Use set to get unique elements
    2. Calculate: 2 * sum(unique) - sum(all)
    3. Result is the single number
    4. This demonstrates mathematical thinking
    """
    # Get unique elements
    unique_nums = set(nums)
    
    # Calculate: 2 * sum(unique) - sum(all)
    return 2 * sum(unique_nums) - sum(nums)


# Test cases to demonstrate all solutions
def test_single_number():
    """Test function to demonstrate all solutions"""
    
    test_cases = [
        [2, 2, 1],
        [4, 1, 2, 1, 2],
        [1],
        [1, 1, 2, 2, 3],
        [0, 0, 1],
    ]
    
    print("=== Single Number Test Cases ===")
    for i, test_case in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        print(f"Input: {test_case}")
        
        # Test all solutions
        result1 = single_number_xor(test_case)
        result2 = single_number_hash_set(test_case)
        result3 = single_number_math(test_case)
        
        print(f"XOR: {result1}")
        print(f"Hash Set: {result2}")
        print(f"Math: {result3}")
        
        # Check if all solutions agree
        all_same = all([result1 == result2, result2 == result3])
        print(f"All solutions agree: {all_same}")


# Main execution
if __name__ == "__main__":
    print("=== Single Number Problem - 3 Solutions ===")
    print("1. XOR (O(n) time, O(1) space) - RECOMMENDED")
    print("2. Hash Set (O(n) time, O(n) space)")
    print("3. Math (O(n) time, O(n) space)")
    print()
    
    # Run test cases
    test_single_number()
    
    print("\n=== Summary ===")
    print("• XOR is most efficient and uses constant space")
    print("• Hash Set is straightforward but uses extra space")
    print("• Math approach shows mathematical thinking")
    print("• All solutions handle edge cases properly")