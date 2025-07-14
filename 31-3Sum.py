"""
Problem: 3Sum
Difficulty: Medium
Category: Arrays & Strings

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that 
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
The triplets [-1,0,1] and [-1,-1,2] have a sum of 0.

Time Complexity Analysis:
- Solution 1 (Brute Force): O(n³) time, O(1) space
- Solution 2 (Hash Set): O(n²) time, O(n) space
- Solution 3 (Two Pointers): O(n²) time, O(1) space (excluding output space)
"""

def three_sum_brute_force(nums):
    """
    Solution 1: Brute Force Approach
    Time Complexity: O(n³) - We check every possible triplet
    Space Complexity: O(1) - Only using a constant amount of extra space
    
    Algorithm:
    1. Use three nested loops to check every possible triplet
    2. If sum equals 0, add to result (avoiding duplicates)
    3. This is the most straightforward but least efficient approach
    """
    n = len(nums)  # Get the length of the array
    result = []  # Store the result triplets
    
    # Three nested loops to check every possible triplet
    for i in range(n - 2):  # First number
        for j in range(i + 1, n - 1):  # Second number
            for k in range(j + 1, n):  # Third number
                # Check if current triplet sums to 0
                if nums[i] + nums[j] + nums[k] == 0:
                    # Create sorted triplet to avoid duplicates
                    triplet = sorted([nums[i], nums[j], nums[k]])
                    # Only add if not already in result
                    if triplet not in result:
                        result.append(triplet)
    
    return result


def three_sum_hash_set(nums):
    """
    Solution 2: Hash Set Approach
    Time Complexity: O(n²) - We use two loops and hash set lookup
    Space Complexity: O(n) - We store numbers in hash set
    
    Algorithm:
    1. Use two nested loops to fix two numbers
    2. Use hash set to find the third number that makes sum 0
    3. This reduces one loop using hash set lookup
    """
    n = len(nums)  # Get the length of the array
    result = []  # Store the result triplets
    
    # Two nested loops to fix two numbers
    for i in range(n - 2):  # First number
        for j in range(i + 1, n - 1):  # Second number
            # Calculate the complement we need
            complement = -(nums[i] + nums[j])
            
            # Check if complement exists in remaining array
            if complement in nums[j + 1:]:
                # Create sorted triplet to avoid duplicates
                triplet = sorted([nums[i], nums[j], complement])
                # Only add if not already in result
                if triplet not in result:
                    result.append(triplet)
    
    return result


def three_sum_two_pointers(nums):
    """
    Solution 3: Two Pointers Approach (Most Efficient)
    Time Complexity: O(n²) - We sort once O(n log n), then two loops O(n²)
    Space Complexity: O(1) - Only using a constant amount of extra space (excluding output)
    
    Algorithm:
    1. Sort the array first
    2. Use one loop to fix the first number
    3. Use two pointers to find the other two numbers
    4. Skip duplicates to avoid duplicate triplets
    5. This is the most efficient approach
    """
    n = len(nums)  # Get the length of the array
    result = []  # Store the result triplets
    
    # Sort the array first (required for two pointers approach)
    nums.sort()
    
    # Use one loop to fix the first number
    for i in range(n - 2):
        # Skip duplicates for the first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Use two pointers for the remaining two numbers
        left = i + 1  # Start from next position
        right = n - 1  # Start from end
        
        # Continue while pointers haven't met
        while left < right:
            # Calculate current sum
            current_sum = nums[i] + nums[left] + nums[right]
            
            # If we found a triplet
            if current_sum == 0:
                # Add to result
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates for left pointer
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                
                # Skip duplicates for right pointer
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                # Move pointers inward
                left += 1
                right -= 1
            
            # If sum is less than 0, move left pointer right (to increase sum)
            elif current_sum < 0:
                left += 1
            
            # If sum is greater than 0, move right pointer left (to decrease sum)
            else:
                right -= 1
    
    return result


def three_sum_optimized(nums):
    """
    Solution 4: Optimized Two Pointers with Early Exit
    Time Complexity: O(n²) - Same as two pointers but with optimizations
    Space Complexity: O(1) - Only constant extra space
    
    Algorithm:
    1. Sort the array
    2. Add early exit conditions for better performance
    3. Skip unnecessary iterations
    4. This is the most optimized version
    """
    n = len(nums)  # Get the length of the array
    result = []  # Store the result triplets
    
    # Sort the array
    nums.sort()
    
    # Early exit if array is too short
    if n < 3:
        return result
    
    # Use one loop to fix the first number
    for i in range(n - 2):
        # Skip duplicates for the first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Early exit if first number is too large (since array is sorted)
        if nums[i] > 0:
            break
        
        # Early exit if sum of three smallest numbers is too large
        if nums[i] + nums[i + 1] + nums[i + 2] > 0:
            break
        
        # Early exit if sum of current number and two largest numbers is too small
        if nums[i] + nums[n - 2] + nums[n - 1] < 0:
            continue
        
        # Use two pointers for the remaining two numbers
        left = i + 1
        right = n - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            
            elif current_sum < 0:
                left += 1
            else:
                right -= 1
    
    return result


# Test cases to demonstrate all solutions
def test_three_sum():
    """Test function to demonstrate all solutions"""
    
    test_cases = [
        [-1, 0, 1, 2, -1, -4],
        [],
        [0],
        [0, 0, 0],
        [1, 2, 3],
        [-2, 0, 1, 1, 2],
        [-1, 0, 1, 2, -1, -4, 0, 0]
    ]
    
    print("=== 3Sum Test Cases ===")
    for i, test_case in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        print(f"Input: {test_case}")
        
        # Test all solutions
        result1 = three_sum_brute_force(test_case.copy())
        result2 = three_sum_hash_set(test_case.copy())
        result3 = three_sum_two_pointers(test_case.copy())
        result4 = three_sum_optimized(test_case.copy())
        
        print(f"Brute Force: {result1}")
        print(f"Hash Set: {result2}")
        print(f"Two Pointers: {result3}")
        print(f"Optimized: {result4}")
        
        # Check if all solutions agree (sorting for comparison)
        all_same = (sorted(result1) == sorted(result2) == 
                   sorted(result3) == sorted(result4))
        print(f"All solutions agree: {all_same}")


# Interactive demo
def interactive_demo():
    """Interactive demo where user can input their own test cases"""
    print("\n=== 3Sum - Interactive Demo ===")
    print("Enter integers separated by spaces (e.g., -1 0 1 2 -1 -4):")
    
    try:
        # Get input from user
        nums_input = input("Numbers: ").strip()
        if nums_input:
            nums = [int(x) for x in nums_input.split()]
        else:
            nums = []
        
        print(f"\nResults for {nums}:")
        print(f"Brute Force: {three_sum_brute_force(nums.copy())}")
        print(f"Hash Set: {three_sum_hash_set(nums.copy())}")
        print(f"Two Pointers: {three_sum_two_pointers(nums.copy())}")
        print(f"Optimized: {three_sum_optimized(nums.copy())}")
        
    except ValueError:
        print("Invalid input! Please enter valid integers.")


# Performance comparison
def performance_comparison():
    """Compare performance of different approaches"""
    import time
    import random
    
    # Create a test array
    nums = [random.randint(-10, 10) for _ in range(20)]
    
    solutions = [
        ("Brute Force", three_sum_brute_force),
        ("Hash Set", three_sum_hash_set),
        ("Two Pointers", three_sum_two_pointers),
        ("Optimized", three_sum_optimized)
    ]
    
    print("\n=== Performance Comparison ===")
    print(f"Testing with array of length {len(nums)}: {nums}")
    
    for name, func in solutions:
        start_time = time.time()
        result = func(nums.copy())
        end_time = time.time()
        
        print(f"{name}: {len(result)} triplets found in {(end_time - start_time)*1000:.2f} ms")


# Edge cases test
def test_edge_cases():
    """Test edge cases"""
    print("\n=== Edge Cases Test ===")
    
    edge_cases = [
        [],  # Empty array
        [1],  # Single element
        [1, 2],  # Two elements
        [0, 0, 0],  # All zeros
        [1, 1, 1],  # All same positive
        [-1, -1, -1],  # All same negative
        [0, 0, 0, 0],  # Multiple zeros
        list(range(-5, 6))  # Range of numbers
    ]
    
    for i, test_case in enumerate(edge_cases, 1):
        print(f"\nEdge Case {i}: {test_case}")
        result = three_sum_two_pointers(test_case.copy())
        print(f"Result: {result}")


# Main execution
if __name__ == "__main__":
    print("=== 3Sum Problem - 4 Solutions ===")
    print("1. Brute Force (O(n³) time, O(1) space)")
    print("2. Hash Set (O(n²) time, O(n) space)")
    print("3. Two Pointers (O(n²) time, O(1) space) - RECOMMENDED")
    print("4. Optimized Two Pointers (O(n²) time, O(1) space)")
    print()
    
    # Run test cases
    test_three_sum()
    
    # Test edge cases
    test_edge_cases()
    
    # Performance comparison
    performance_comparison()
    
    # Ask if user wants interactive demo
    choice = input("\nWould you like to try your own test case? (y/n): ").lower()
    if choice == 'y':
        interactive_demo()
    
    print("\n=== Summary ===")
    print("• Two Pointers is most efficient for this problem")
    print("• Brute Force is simple but very inefficient")
    print("• Hash Set provides a middle ground")
    print("• Optimized version adds early exits for better performance")
    print("• All solutions handle duplicates properly")
    print("• Sorting is key for the efficient solutions")