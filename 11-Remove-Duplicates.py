"""
Problem: Remove Duplicates from Sorted Array
Difficulty: Easy
Category: Arrays & Strings

Given a sorted array nums, remove the duplicates in-place such that each element 
appears only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying 
the input array in-place with O(1) extra memory.

Example:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return length = 2, with the first two elements 
of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the returned length.

Time Complexity Analysis:
- Solution 1 (Two Pointers): O(n) time, O(1) space
- Solution 2 (Set Approach): O(n) time, O(n) space (not in-place)
- Solution 3 (List Comprehension): O(n) time, O(n) space (not in-place)
"""

def remove_duplicates_two_pointers(nums):
    """
    Solution 1: Two Pointers Approach (Most Efficient)
    Time Complexity: O(n) - We traverse the array once
    Space Complexity: O(1) - We only use a constant amount of extra space
    
    Algorithm:
    1. Use two pointers: one for current position, one for next unique element
    2. Compare current element with next element
    3. If different, move unique element to current position
    4. Continue until end of array
    5. This is the most efficient in-place solution
    """
    # Handle empty array
    if not nums:
        return 0
    
    # Initialize pointer for unique elements
    unique_index = 0
    
    # Traverse array starting from second element
    for i in range(1, len(nums)):
        # If current element is different from previous unique element
        if nums[i] != nums[unique_index]:
            unique_index += 1  # Move to next position
            nums[unique_index] = nums[i]  # Place unique element
    
    # Return length of unique elements (index + 1)
    return unique_index + 1


def remove_duplicates_set_approach(nums):
    """
    Solution 2: Set Approach (Not In-place)
    Time Complexity: O(n) - We process each element once
    Space Complexity: O(n) - We use a set to store unique elements
    
    Algorithm:
    1. Convert array to set to remove duplicates
    2. Convert back to list
    3. Update original array
    4. This is not in-place but shows set usage
    """
    # Convert to set and back to list
    unique_nums = list(set(nums))
    
    # Sort to maintain order (since original was sorted)
    unique_nums.sort()
    
    # Update original array
    for i in range(len(unique_nums)):
        nums[i] = unique_nums[i]
    
    # Fill remaining positions with placeholder (optional)
    for i in range(len(unique_nums), len(nums)):
        nums[i] = '_'
    
    return len(unique_nums)


def remove_duplicates_list_comprehension(nums):
    """
    Solution 3: List Comprehension Approach (Not In-place)
    Time Complexity: O(n) - We process each element once
    Space Complexity: O(n) - We create a new list
    
    Algorithm:
    1. Use list comprehension to create unique list
    2. Update original array
    3. This demonstrates Pythonic approach
    """
    # Create list of unique elements maintaining order
    unique_nums = []
    for num in nums:
        if num not in unique_nums:
            unique_nums.append(num)
    
    # Update original array
    for i in range(len(unique_nums)):
        nums[i] = unique_nums[i]
    
    # Fill remaining positions with placeholder (optional)
    for i in range(len(unique_nums), len(nums)):
        nums[i] = '_'
    
    return len(unique_nums)


def remove_duplicates_recursive(nums, index=0):
    """
    Solution 4: Recursive Approach
    Time Complexity: O(n) - We process each element once
    Space Complexity: O(n) - Due to recursion call stack
    
    Algorithm:
    1. Use recursion to process array
    2. Base case: end of array
    3. Recursive case: skip duplicates, keep unique
    4. This demonstrates recursive thinking
    """
    # Base case: reached end of array
    if index >= len(nums) - 1:
        return len(nums)
    
    # If current element equals next element, remove next
    if nums[index] == nums[index + 1]:
        # Remove duplicate by shifting elements
        nums.pop(index + 1)
        # Recursively process same position
        return remove_duplicates_recursive(nums, index)
    else:
        # Move to next position
        return remove_duplicates_recursive(nums, index + 1)


def remove_duplicates_optimized(nums):
    """
    Solution 5: Optimized Two Pointers with Early Exit
    Time Complexity: O(n) - We traverse the array once
    Space Complexity: O(1) - Only constant extra space
    
    Algorithm:
    1. Same as two pointers but with optimizations
    2. Early exit for single element arrays
    3. Skip unnecessary operations
    4. This is the most optimized version
    """
    # Handle edge cases
    if not nums:
        return 0
    if len(nums) == 1:
        return 1
    
    # Initialize pointer for unique elements
    unique_index = 0
    
    # Traverse array starting from second element
    for i in range(1, len(nums)):
        # If current element is different from previous unique element
        if nums[i] != nums[unique_index]:
            unique_index += 1  # Move to next position
            # Only swap if positions are different
            if i != unique_index:
                nums[unique_index] = nums[i]
        # If same, just continue (skip duplicate)
    
    # Return length of unique elements (index + 1)
    return unique_index + 1


# Test cases to demonstrate all solutions
def test_remove_duplicates():
    """Test function to demonstrate all solutions"""
    
    test_cases = [
        [1, 1, 2],
        [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
        [1, 2, 3],
        [1, 1, 1, 1],
        [1],
        [],
        [1, 2, 2, 3, 3, 3, 4, 4, 4, 4],
    ]
    
    print("=== Remove Duplicates Test Cases ===")
    for i, test_case in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        print(f"Input: {test_case}")
        
        # Test all solutions
        result1 = remove_duplicates_two_pointers(test_case.copy())
        result2 = remove_duplicates_set_approach(test_case.copy())
        result3 = remove_duplicates_list_comprehension(test_case.copy())
        result4 = remove_duplicates_recursive(test_case.copy())
        result5 = remove_duplicates_optimized(test_case.copy())
        
        print(f"Two Pointers: {result1}")
        print(f"Set Approach: {result2}")
        print(f"List Comprehension: {result3}")
        print(f"Recursive: {result4}")
        print(f"Optimized: {result5}")
        
        # Check if all solutions agree
        all_same = all([result1 == result2, result2 == result3, 
                       result3 == result4, result4 == result5])
        print(f"All solutions agree: {all_same}")


# Interactive demo
def interactive_demo():
    """Interactive demo where user can input their own test cases"""
    print("\n=== Remove Duplicates - Interactive Demo ===")
    print("Enter sorted integers separated by spaces (e.g., 1 1 2 2 3):")
    
    try:
        # Get input from user
        nums_input = input("Numbers: ").strip()
        if nums_input:
            nums = [int(x) for x in nums_input.split()]
        else:
            nums = []
        
        print(f"\nOriginal array: {nums}")
        
        # Test all solutions
        print(f"Two Pointers: {remove_duplicates_two_pointers(nums.copy())}")
        print(f"Set Approach: {remove_duplicates_set_approach(nums.copy())}")
        print(f"List Comprehension: {remove_duplicates_list_comprehension(nums.copy())}")
        print(f"Recursive: {remove_duplicates_recursive(nums.copy())}")
        print(f"Optimized: {remove_duplicates_optimized(nums.copy())}")
        
    except ValueError:
        print("Invalid input! Please enter valid integers.")


# Main execution
if __name__ == "__main__":
    print("=== Remove Duplicates Problem - 5 Solutions ===")
    print("1. Two Pointers (O(n) time, O(1) space) - RECOMMENDED")
    print("2. Set Approach (O(n) time, O(n) space)")
    print("3. List Comprehension (O(n) time, O(n) space)")
    print("4. Recursive (O(n) time, O(n) space)")
    print("5. Optimized Two Pointers (O(n) time, O(1) space)")
    print()
    
    # Run test cases
    test_remove_duplicates()
    
    # Ask if user wants interactive demo
    choice = input("\nWould you like to try your own test case? (y/n): ").lower()
    if choice == 'y':
        interactive_demo()
    
    print("\n=== Summary ===")
    print("• Two Pointers is most efficient and in-place")
    print("• Set approach is simple but not in-place")
    print("• List comprehension shows Pythonic approach")
    print("• Recursive demonstrates recursive thinking")
    print("• Optimized version adds performance improvements")
    print("• All solutions handle edge cases properly")