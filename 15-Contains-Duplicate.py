"""
Problem: Contains Duplicate
Difficulty: Easy
Category: Arrays & Strings

Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Example:
Input: nums = [1,2,3,1]
Output: true

Time Complexity Analysis:
- Solution 1 (Hash Set): O(n) time, O(n) space
- Solution 2 (Sort): O(n log n) time, O(1) space
- Solution 3 (Brute Force): O(n²) time, O(1) space
"""

def contains_duplicate_hash_set(nums):
    """
    Solution 1: Hash Set Approach (Most Efficient)
    Time Complexity: O(n) - We traverse the array once
    Space Complexity: O(n) - We use a hash set
    
    Algorithm:
    1. Use hash set to track seen numbers
    2. If number already in set, return true
    3. Otherwise, add to set
    4. This is the most efficient approach
    """
    seen = set()  # Hash set to track seen numbers
    
    # Traverse array
    for num in nums:
        if num in seen:
            return True  # Found duplicate
        seen.add(num)  # Add to set
    
    return False  # No duplicates found


def contains_duplicate_sort(nums):
    """
    Solution 2: Sorting Approach
    Time Complexity: O(n log n) - Due to sorting
    Space Complexity: O(1) - In-place sorting
    
    Algorithm:
    1. Sort the array
    2. Check adjacent elements
    3. If any adjacent elements are equal, return true
    4. This uses less space but is slower
    """
    nums.sort()  # Sort the array
    
    # Check adjacent elements
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True  # Found duplicate
    
    return False  # No duplicates found


def contains_duplicate_brute_force(nums):
    """
    Solution 3: Brute Force Approach
    Time Complexity: O(n²) - We check each pair
    Space Complexity: O(1) - We only use a constant amount of extra space
    
    Algorithm:
    1. Use two nested loops
    2. Compare each element with every other element
    3. If any match found, return true
    4. This is the most straightforward but least efficient
    """
    n = len(nums)  # Length of array
    
    # Check each pair
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True  # Found duplicate
    
    return False  # No duplicates found


# Test cases to demonstrate all solutions
def test_contains_duplicate():
    """Test function to demonstrate all solutions"""
    
    test_cases = [
        [1, 2, 3, 1],
        [1, 2, 3, 4],
        [1, 1, 1, 3, 3, 4, 3, 2, 4, 2],
        [1],
        [],
    ]
    
    print("=== Contains Duplicate Test Cases ===")
    for i, test_case in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        print(f"Input: {test_case}")
        
        # Test all solutions
        result1 = contains_duplicate_hash_set(test_case.copy())
        result2 = contains_duplicate_sort(test_case.copy())
        result3 = contains_duplicate_brute_force(test_case.copy())
        
        print(f"Hash Set: {result1}")
        print(f"Sort: {result2}")
        print(f"Brute Force: {result3}")
        
        # Check if all solutions agree
        all_same = all([result1 == result2, result2 == result3])
        print(f"All solutions agree: {all_same}")


# Main execution
if __name__ == "__main__":
    print("=== Contains Duplicate Problem - 3 Solutions ===")
    print("1. Hash Set (O(n) time, O(n) space) - RECOMMENDED")
    print("2. Sort (O(n log n) time, O(1) space)")
    print("3. Brute Force (O(n²) time, O(1) space)")
    print()
    
    # Run test cases
    test_contains_duplicate()
    
    print("\n=== Summary ===")
    print("• Hash Set is most efficient")
    print("• Sort approach uses less space but is slower")
    print("• Brute Force is straightforward but inefficient")
    print("• All solutions handle edge cases properly")