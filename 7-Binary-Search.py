"""
Problem: Binary Search
Difficulty: Easy
Category: Basic Algorithms

Given a sorted array of integers nums and an integer target, write a function to search 
target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Time Complexity Analysis:
- Solution 1 (Iterative): O(log n) time, O(1) space
- Solution 2 (Recursive): O(log n) time, O(log n) space (due to call stack)
- Solution 3 (Built-in): O(log n) time, O(1) space
"""

def binary_search_iterative(nums, target):
    """
    Solution 1: Iterative Binary Search (Most Efficient)
    Time Complexity: O(log n) - We halve the search space in each iteration
    Space Complexity: O(1) - We only use a constant amount of extra space
    
    Algorithm:
    1. Initialize left and right pointers
    2. While left <= right, calculate middle
    3. If middle element equals target, return index
    4. If middle element < target, search right half
    5. If middle element > target, search left half
    6. If not found, return -1
    """
    # Initialize pointers
    left = 0  # Start of array
    right = len(nums) - 1  # End of array
    
    # Continue while search space is valid
    while left <= right:
        # Calculate middle index (prevents integer overflow)
        mid = left + (right - left) // 2
        
        # If we found the target
        if nums[mid] == target:
            return mid
        
        # If middle element is less than target, search right half
        elif nums[mid] < target:
            left = mid + 1
        
        # If middle element is greater than target, search left half
        else:
            right = mid - 1
    
    # Target not found
    return -1


def binary_search_recursive(nums, target, left=0, right=None):
    """
    Solution 2: Recursive Binary Search
    Time Complexity: O(log n) - We halve the search space in each recursive call
    Space Complexity: O(log n) - Due to call stack depth
    
    Algorithm:
    1. Base case: if left > right, return -1
    2. Calculate middle index
    3. If middle element equals target, return index
    4. Recursively search left or right half
    5. This demonstrates recursive thinking
    """
    # Initialize right pointer if not provided
    if right is None:
        right = len(nums) - 1
    
    # Base case: search space is invalid
    if left > right:
        return -1
    
    # Calculate middle index
    mid = left + (right - left) // 2
    
    # If we found the target
    if nums[mid] == target:
        return mid
    
    # If middle element is less than target, search right half
    elif nums[mid] < target:
        return binary_search_recursive(nums, target, mid + 1, right)
    
    # If middle element is greater than target, search left half
    else:
        return binary_search_recursive(nums, target, left, mid - 1)


def binary_search_builtin(nums, target):
    """
    Solution 3: Using Python's Built-in bisect Module
    Time Complexity: O(log n) - Same as binary search
    Space Complexity: O(1) - Only constant extra space
    
    Algorithm:
    1. Use bisect.bisect_left to find insertion point
    2. Check if target exists at that position
    3. This is the most Pythonic approach
    """
    import bisect
    
    # Find the insertion point for target
    index = bisect.bisect_left(nums, target)
    
    # Check if target exists at the insertion point
    if index < len(nums) and nums[index] == target:
        return index
    
    # Target not found
    return -1


def binary_search_first_occurrence(nums, target):
    """
    Solution 4: Find First Occurrence (Advanced)
    Time Complexity: O(log n) - Same as binary search
    Space Complexity: O(1) - Only constant extra space
    
    Algorithm:
    1. Modified binary search to find first occurrence
    2. When we find target, continue searching left half
    3. This is useful when array has duplicates
    """
    left = 0
    right = len(nums) - 1
    result = -1  # Store the result
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            result = mid  # Store this occurrence
            right = mid - 1  # Continue searching left half for earlier occurrence
        
        elif nums[mid] < target:
            left = mid + 1
        
        else:
            right = mid - 1
    
    return result


def binary_search_last_occurrence(nums, target):
    """
    Solution 5: Find Last Occurrence (Advanced)
    Time Complexity: O(log n) - Same as binary search
    Space Complexity: O(1) - Only constant extra space
    
    Algorithm:
    1. Modified binary search to find last occurrence
    2. When we find target, continue searching right half
    3. This is useful when array has duplicates
    """
    left = 0
    right = len(nums) - 1
    result = -1  # Store the result
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            result = mid  # Store this occurrence
            left = mid + 1  # Continue searching right half for later occurrence
        
        elif nums[mid] < target:
            left = mid + 1
        
        else:
            right = mid - 1
    
    return result


# Test cases to demonstrate all solutions
def test_binary_search():
    """Test function to demonstrate all solutions"""
    
    test_cases = [
        ([-1, 0, 3, 5, 9, 12], 9),  # Target exists
        ([-1, 0, 3, 5, 9, 12], 2),  # Target doesn't exist
        ([1, 2, 3, 4, 5], 1),  # Target at beginning
        ([1, 2, 3, 4, 5], 5),  # Target at end
        ([1], 1),  # Single element, target exists
        ([1], 2),  # Single element, target doesn't exist
        ([], 1),  # Empty array
        ([1, 1, 1, 1, 1], 1),  # All same elements
        ([1, 2, 2, 2, 3], 2),  # Multiple occurrences
    ]
    
    print("=== Binary Search Test Cases ===")
    for i, (nums, target) in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        print(f"Array: {nums}, Target: {target}")
        
        # Test all solutions
        result1 = binary_search_iterative(nums, target)
        result2 = binary_search_recursive(nums, target)
        result3 = binary_search_builtin(nums, target)
        result4 = binary_search_first_occurrence(nums, target)
        result5 = binary_search_last_occurrence(nums, target)
        
        print(f"Iterative: {result1}")
        print(f"Recursive: {result2}")
        print(f"Built-in: {result3}")
        print(f"First Occurrence: {result4}")
        print(f"Last Occurrence: {result5}")
        
        # Check if basic solutions agree
        basic_same = all([result1 == result2, result2 == result3])
        print(f"Basic solutions agree: {basic_same}")


# Interactive demo
def interactive_demo():
    """Interactive demo where user can input their own test cases"""
    print("\n=== Binary Search - Interactive Demo ===")
    print("Enter sorted integers separated by spaces (e.g., 1 2 3 4 5):")
    
    try:
        # Get array input from user
        nums_input = input("Sorted Array: ").strip()
        if nums_input:
            nums = [int(x) for x in nums_input.split()]
        else:
            nums = []
        
        # Get target from user
        target = int(input("Target: "))
        
        print(f"\nResults for array {nums} with target {target}:")
        print(f"Iterative: {binary_search_iterative(nums, target)}")
        print(f"Recursive: {binary_search_recursive(nums, target)}")
        print(f"Built-in: {binary_search_builtin(nums, target)}")
        print(f"First Occurrence: {binary_search_first_occurrence(nums, target)}")
        print(f"Last Occurrence: {binary_search_last_occurrence(nums, target)}")
        
    except ValueError:
        print("Invalid input! Please enter valid integers.")


# Performance comparison
def performance_comparison():
    """Compare performance of different approaches"""
    import time
    import random
    
    # Create a large sorted array
    nums = sorted([random.randint(1, 1000) for _ in range(10000)])
    target = random.choice(nums)  # Target that exists
    
    solutions = [
        ("Iterative", binary_search_iterative),
        ("Recursive", binary_search_recursive),
        ("Built-in", binary_search_builtin),
        ("First Occurrence", binary_search_first_occurrence),
        ("Last Occurrence", binary_search_last_occurrence)
    ]
    
    print("\n=== Performance Comparison ===")
    print(f"Testing with array of length {len(nums)}")
    print(f"Target: {target}")
    
    for name, func in solutions:
        start_time = time.time()
        result = func(nums, target)
        end_time = time.time()
        
        print(f"{name}: {result} (Time: {(end_time - start_time)*1000:.2f} ms)")


# Binary search visualization
def binary_search_visualization(nums, target):
    """Show step-by-step binary search process"""
    print(f"\n=== Binary Search Visualization ===")
    print(f"Array: {nums}")
    print(f"Target: {target}")
    print()
    
    left = 0
    right = len(nums) - 1
    step = 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        # Create visual representation
        visual = [' '] * len(nums)
        visual[left] = 'L'
        visual[right] = 'R'
        visual[mid] = 'M'
        
        print(f"Step {step}:")
        print(f"Indices: {list(range(len(nums)))}")
        print(f"Values:  {nums}")
        print(f"Pointers: {visual}")
        print(f"Left={left}, Right={right}, Mid={mid}, nums[mid]={nums[mid]}")
        
        if nums[mid] == target:
            print(f"✓ Found target at index {mid}")
            break
        elif nums[mid] < target:
            print(f"→ nums[mid] < target, search right half")
            left = mid + 1
        else:
            print(f"→ nums[mid] > target, search left half")
            right = mid - 1
        
        step += 1
        print()
    
    if left > right:
        print("✗ Target not found")


# Main execution
if __name__ == "__main__":
    print("=== Binary Search Problem - 5 Solutions ===")
    print("1. Iterative (O(log n) time, O(1) space) - RECOMMENDED")
    print("2. Recursive (O(log n) time, O(log n) space)")
    print("3. Built-in bisect (O(log n) time, O(1) space)")
    print("4. First Occurrence (O(log n) time, O(1) space)")
    print("5. Last Occurrence (O(log n) time, O(1) space)")
    print()
    
    # Run test cases
    test_binary_search()
    
    # Visualization demo
    binary_search_visualization([1, 3, 5, 7, 9, 11, 13, 15], 7)
    
    # Performance comparison
    performance_comparison()
    
    # Ask if user wants interactive demo
    choice = input("\nWould you like to try your own test case? (y/n): ").lower()
    if choice == 'y':
        interactive_demo()
    
    print("\n=== Summary ===")
    print("• Iterative is most space-efficient")
    print("• Recursive is most elegant")
    print("• Built-in is most Pythonic")
    print("• First/Last occurrence handle duplicates")
    print("• All solutions require sorted array")
    print("• Time complexity is always O(log n)")