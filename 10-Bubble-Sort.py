"""
Problem: Bubble Sort
Difficulty: Easy
Category: Basic Algorithms

Implement bubble sort algorithm to sort an array in ascending order.

Bubble Sort is a simple sorting algorithm that repeatedly steps through the list,
compares adjacent elements and swaps them if they are in the wrong order.

Example:
Input: [64, 34, 25, 12, 22, 11, 90]
Output: [11, 12, 22, 25, 34, 64, 90]

Time Complexity Analysis:
- Best Case: O(n) - When array is already sorted
- Average Case: O(n²) - When array is partially sorted
- Worst Case: O(n²) - When array is reverse sorted
- Space Complexity: O(1) - In-place sorting
"""

def bubble_sort_basic(arr):
    """
    Solution 1: Basic Bubble Sort
    Time Complexity: O(n²) - Always performs n² comparisons
    Space Complexity: O(1) - In-place sorting
    
    Algorithm:
    1. Compare adjacent elements
    2. Swap if they are in wrong order
    3. Repeat for all pairs
    4. After each pass, largest element bubbles to end
    5. This is the most straightforward implementation
    """
    n = len(arr)  # Get array length
    
    # Outer loop: number of passes needed
    for i in range(n):
        # Inner loop: compare adjacent elements
        for j in range(0, n - i - 1):
            # If current element is greater than next, swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr


def bubble_sort_optimized(arr):
    """
    Solution 2: Optimized Bubble Sort
    Time Complexity: O(n²) worst case, O(n) best case
    Space Complexity: O(1) - In-place sorting
    
    Algorithm:
    1. Add a flag to track if any swaps occurred
    2. If no swaps in a pass, array is sorted
    3. Early termination when array is sorted
    4. This improves performance for partially sorted arrays
    """
    n = len(arr)  # Get array length
    
    # Outer loop: number of passes needed
    for i in range(n):
        # Flag to track if any swaps occurred
        swapped = False
        
        # Inner loop: compare adjacent elements
        for j in range(0, n - i - 1):
            # If current element is greater than next, swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swaps occurred, array is sorted
        if not swapped:
            break
    
    return arr


def bubble_sort_recursive(arr, n=None):
    """
    Solution 3: Recursive Bubble Sort
    Time Complexity: O(n²) - Same as iterative
    Space Complexity: O(n) - Due to recursion call stack
    
    Algorithm:
    1. Base case: if array has 1 element, it's sorted
    2. Recursive case: bubble largest element to end
    3. Recursively sort remaining n-1 elements
    4. This demonstrates recursive thinking
    """
    # Initialize n if not provided
    if n is None:
        n = len(arr)
    
    # Base case: if array has 1 element, it's sorted
    if n == 1:
        return arr
    
    # Bubble largest element to end
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    # Recursively sort remaining n-1 elements
    bubble_sort_recursive(arr, n - 1)
    
    return arr


def bubble_sort_visualization(arr):
    """
    Solution 4: Bubble Sort with Visualization
    Time Complexity: O(n²) - Same as basic bubble sort
    Space Complexity: O(1) - In-place sorting
    
    Algorithm:
    1. Same as basic bubble sort
    2. Add visualization to show sorting process
    3. Useful for understanding the algorithm
    """
    n = len(arr)  # Get array length
    
    print("Original array:", arr)
    print("Starting bubble sort...")
    
    # Outer loop: number of passes needed
    for i in range(n):
        print(f"\nPass {i + 1}:")
        
        # Inner loop: compare adjacent elements
        for j in range(0, n - i - 1):
            # Show current comparison
            print(f"  Comparing {arr[j]} and {arr[j + 1]}")
            
            # If current element is greater than next, swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(f"  Swapped! Array: {arr}")
            else:
                print(f"  No swap needed")
        
        print(f"After pass {i + 1}: {arr}")
    
    print(f"\nFinal sorted array: {arr}")
    return arr


def bubble_sort_comparison_count(arr):
    """
    Solution 5: Bubble Sort with Comparison Count
    Time Complexity: O(n²) - Same as basic bubble sort
    Space Complexity: O(1) - In-place sorting
    
    Algorithm:
    1. Same as basic bubble sort
    2. Count number of comparisons and swaps
    3. Useful for performance analysis
    """
    n = len(arr)  # Get array length
    comparisons = 0  # Count comparisons
    swaps = 0  # Count swaps
    
    # Outer loop: number of passes needed
    for i in range(n):
        # Inner loop: compare adjacent elements
        for j in range(0, n - i - 1):
            comparisons += 1  # Increment comparison count
            
            # If current element is greater than next, swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1  # Increment swap count
    
    print(f"Comparisons: {comparisons}")
    print(f"Swaps: {swaps}")
    return arr


# Test cases to demonstrate all solutions
def test_bubble_sort():
    """Test function to demonstrate all solutions"""
    
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [1, 2, 3, 4, 5],  # Already sorted
        [5, 4, 3, 2, 1],  # Reverse sorted
        [1],  # Single element
        [],  # Empty array
        [3, 3, 3, 3],  # All same elements
        [1, 2, 2, 1],  # Duplicates
    ]
    
    print("=== Bubble Sort Test Cases ===")
    for i, test_case in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        print(f"Input: {test_case}")
        
        # Test all solutions
        result1 = bubble_sort_basic(test_case.copy())
        result2 = bubble_sort_optimized(test_case.copy())
        result3 = bubble_sort_recursive(test_case.copy())
        result4 = bubble_sort_comparison_count(test_case.copy())
        
        print(f"Basic: {result1}")
        print(f"Optimized: {result2}")
        print(f"Recursive: {result3}")
        print(f"With Count: {result4}")
        
        # Check if all solutions agree
        all_same = all([result1 == result2, result2 == result3, result3 == result4])
        print(f"All solutions agree: {all_same}")


# Performance comparison
def performance_comparison():
    """Compare performance of different bubble sort implementations"""
    import time
    import random
    
    # Create test arrays of different sizes
    test_sizes = [100, 500, 1000]
    
    print("\n=== Performance Comparison ===")
    
    for size in test_sizes:
        print(f"\nArray size: {size}")
        
        # Create random array
        arr = [random.randint(1, 1000) for _ in range(size)]
        
        solutions = [
            ("Basic", bubble_sort_basic),
            ("Optimized", bubble_sort_optimized),
            ("Recursive", bubble_sort_recursive),
        ]
        
        for name, func in solutions:
            test_arr = arr.copy()
            start_time = time.time()
            result = func(test_arr)
            end_time = time.time()
            
            print(f"{name}: {(end_time - start_time)*1000:.2f} ms")


# Interactive demo
def interactive_demo():
    """Interactive demo where user can input their own test cases"""
    print("\n=== Bubble Sort - Interactive Demo ===")
    print("Enter integers separated by spaces (e.g., 64 34 25 12 22 11 90):")
    
    try:
        # Get input from user
        nums_input = input("Numbers: ").strip()
        if nums_input:
            nums = [int(x) for x in nums_input.split()]
        else:
            nums = []
        
        print(f"\nOriginal array: {nums}")
        
        # Test all solutions
        print(f"Basic: {bubble_sort_basic(nums.copy())}")
        print(f"Optimized: {bubble_sort_optimized(nums.copy())}")
        print(f"Recursive: {bubble_sort_recursive(nums.copy())}")
        
        # Show visualization
        print("\nVisualization:")
        bubble_sort_visualization(nums.copy())
        
    except ValueError:
        print("Invalid input! Please enter valid integers.")


# Main execution
if __name__ == "__main__":
    print("=== Bubble Sort Problem - 5 Solutions ===")
    print("1. Basic (O(n²) time, O(1) space)")
    print("2. Optimized (O(n²) worst, O(n) best time, O(1) space) - RECOMMENDED")
    print("3. Recursive (O(n²) time, O(n) space)")
    print("4. Visualization (O(n²) time, O(1) space)")
    print("5. Comparison Count (O(n²) time, O(1) space)")
    print()
    
    # Run test cases
    test_bubble_sort()
    
    # Performance comparison
    performance_comparison()
    
    # Ask if user wants interactive demo
    choice = input("\nWould you like to try your own test case? (y/n): ").lower()
    if choice == 'y':
        interactive_demo()
    
    print("\n=== Summary ===")
    print("• Optimized version is most efficient")
    print("• Basic version is most straightforward")
    print("• Recursive shows elegant recursive thinking")
    print("• Visualization helps understand the process")
    print("• All solutions handle edge cases properly")
    print("• Bubble sort is not efficient for large arrays")