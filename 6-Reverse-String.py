"""
Problem: Reverse String
Difficulty: Easy
Category: Arrays & Strings

Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Example:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Time Complexity Analysis:
- Solution 1 (Two Pointers): O(n) time, O(1) space
- Solution 2 (Python Slicing): O(n) time, O(1) space (but creates new list)
- Solution 3 (Recursive): O(n) time, O(n) space (due to call stack)
"""

def reverse_string_two_pointers(s):
    """
    Solution 1: Two Pointers Approach (Most Efficient)
    Time Complexity: O(n) - We swap n/2 pairs of characters
    Space Complexity: O(1) - We only use a constant amount of extra space
    
    Algorithm:
    1. Use two pointers: one at start, one at end
    2. Swap characters at both pointers
    3. Move pointers inward until they meet
    4. This is the most efficient in-place solution
    """
    # Convert string to list if it's a string
    if isinstance(s, str):
        s = list(s)
    
    # Initialize two pointers
    left = 0  # Start from beginning
    right = len(s) - 1  # Start from end
    
    # Continue while pointers haven't met
    while left < right:
        # Swap characters at both pointers
        s[left], s[right] = s[right], s[left]
        
        # Move pointers inward
        left += 1
        right -= 1
    
    return s


def reverse_string_slicing(s):
    """
    Solution 2: Python Slicing Approach
    Time Complexity: O(n) - Python creates a new reversed list
    Space Complexity: O(n) - Creates a new list (not truly in-place)
    
    Algorithm:
    1. Use Python's slice notation with step -1
    2. This is the most Pythonic approach
    3. Note: This creates a new list, so it's not truly in-place
    """
    # Convert string to list if it's a string
    if isinstance(s, str):
        s = list(s)
    
    # Use slice notation to reverse
    return s[::-1]


def reverse_string_recursive(s, left=0):
    """
    Solution 3: Recursive Approach
    Time Complexity: O(n) - We make n/2 recursive calls
    Space Complexity: O(n) - Due to call stack depth
    
    Algorithm:
    1. Use recursion to swap characters from both ends
    2. Base case: when left pointer reaches or passes middle
    3. Recursive case: swap and call recursively with left+1
    4. This demonstrates recursive thinking
    """
    # Convert string to list if it's a string
    if isinstance(s, str):
        s = list(s)
    
    # Calculate right pointer
    right = len(s) - 1 - left
    
    # Base case: if left pointer has reached or passed the middle
    if left >= right:
        return s
    
    # Recursive case: swap characters and recurse
    s[left], s[right] = s[right], s[left]
    return reverse_string_recursive(s, left + 1)


def reverse_string_stack_approach(s):
    """
    Solution 4: Stack Approach (Not in-place, but educational)
    Time Complexity: O(n) - We push and pop each character once
    Space Complexity: O(n) - We use a stack to store all characters
    
    Algorithm:
    1. Push all characters onto a stack
    2. Pop characters from stack to get reversed order
    3. This demonstrates stack LIFO property
    """
    # Convert string to list if it's a string
    if isinstance(s, str):
        s = list(s)
    
    # Create a stack
    stack = []
    
    # Push all characters onto stack
    for char in s:
        stack.append(char)
    
    # Pop characters from stack to get reversed order
    reversed_chars = []
    while stack:
        reversed_chars.append(stack.pop())
    
    return reversed_chars


def reverse_string_xor_swap(s):
    """
    Solution 5: XOR Swap (Advanced, for educational purposes)
    Time Complexity: O(n) - We swap n/2 pairs
    Space Complexity: O(1) - Only constant extra space
    
    Algorithm:
    1. Use XOR to swap characters without temporary variable
    2. a = a ^ b, b = a ^ b, a = a ^ b
    3. This is a bit manipulation technique
    """
    # Convert string to list if it's a string
    if isinstance(s, str):
        s = list(s)
    
    left = 0
    right = len(s) - 1
    
    while left < right:
        # XOR swap without temporary variable
        s[left] = chr(ord(s[left]) ^ ord(s[right]))
        s[right] = chr(ord(s[left]) ^ ord(s[right]))
        s[left] = chr(ord(s[left]) ^ ord(s[right]))
        
        left += 1
        right -= 1
    
    return s


# Test cases to demonstrate all solutions
def test_reverse_string():
    """Test function to demonstrate all solutions"""
    
    test_cases = [
        ["h", "e", "l", "l", "o"],
        ["H", "a", "n", "n", "a", "h"],
        ["a"],
        [],
        ["a", "b"],
        ["1", "2", "3", "4", "5"],
        ["p", "y", "t", "h", "o", "n"]
    ]
    
    print("=== Reverse String Test Cases ===")
    for i, test_case in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        print(f"Input: {test_case}")
        
        # Test all solutions
        result1 = reverse_string_two_pointers(test_case.copy())
        result2 = reverse_string_slicing(test_case.copy())
        result3 = reverse_string_recursive(test_case.copy())
        result4 = reverse_string_stack_approach(test_case.copy())
        result5 = reverse_string_xor_swap(test_case.copy())
        
        print(f"Two Pointers: {result1}")
        print(f"Slicing: {result2}")
        print(f"Recursive: {result3}")
        print(f"Stack: {result4}")
        print(f"XOR Swap: {result5}")
        
        # Check if all solutions agree
        all_same = all([result1 == result2, result2 == result3, 
                       result3 == result4, result4 == result5])
        print(f"All solutions agree: {all_same}")


# Interactive demo
def interactive_demo():
    """Interactive demo where user can input their own test cases"""
    print("\n=== Reverse String - Interactive Demo ===")
    print("Enter characters separated by spaces (e.g., h e l l o):")
    
    try:
        # Get input from user
        chars_input = input("Characters: ").strip()
        if chars_input:
            chars = chars_input.split()
        else:
            chars = []
        
        print(f"\nResults for {chars}:")
        print(f"Two Pointers: {reverse_string_two_pointers(chars.copy())}")
        print(f"Slicing: {reverse_string_slicing(chars.copy())}")
        print(f"Recursive: {reverse_string_recursive(chars.copy())}")
        print(f"Stack: {reverse_string_stack_approach(chars.copy())}")
        print(f"XOR Swap: {reverse_string_xor_swap(chars.copy())}")
        
    except Exception as e:
        print(f"Error: {e}")


# Performance comparison
def performance_comparison():
    """Compare performance of different approaches"""
    import time
    
    # Create a long test string
    test_string = list("abcdefghijklmnopqrstuvwxyz" * 100)
    
    solutions = [
        ("Two Pointers", reverse_string_two_pointers),
        ("Slicing", reverse_string_slicing),
        ("Recursive", reverse_string_recursive),
        ("Stack", reverse_string_stack_approach),
        ("XOR Swap", reverse_string_xor_swap)
    ]
    
    print("\n=== Performance Comparison ===")
    print(f"Testing with string of length {len(test_string)}")
    
    for name, func in solutions:
        start_time = time.time()
        result = func(test_string.copy())
        end_time = time.time()
        
        print(f"{name}: {(end_time - start_time)*1000:.2f} ms")


# String-specific test
def test_string_inputs():
    """Test with actual string inputs"""
    print("\n=== Testing with String Inputs ===")
    
    test_strings = ["hello", "python", "algorithm", "racecar", ""]
    
    for test_str in test_strings:
        print(f"\nInput string: '{test_str}'")
        print(f"Two Pointers: {''.join(reverse_string_two_pointers(test_str))}")
        print(f"Slicing: {''.join(reverse_string_slicing(test_str))}")
        print(f"Recursive: {''.join(reverse_string_recursive(test_str))}")


# Main execution
if __name__ == "__main__":
    print("=== Reverse String Problem - 5 Solutions ===")
    print("1. Two Pointers (O(n) time, O(1) space) - RECOMMENDED")
    print("2. Python Slicing (O(n) time, O(n) space)")
    print("3. Recursive (O(n) time, O(n) space)")
    print("4. Stack Approach (O(n) time, O(n) space)")
    print("5. XOR Swap (O(n) time, O(1) space) - Advanced")
    print()
    
    # Run test cases
    test_reverse_string()
    
    # Test with string inputs
    test_string_inputs()
    
    # Performance comparison
    performance_comparison()
    
    # Ask if user wants interactive demo
    choice = input("\nWould you like to try your own test case? (y/n): ").lower()
    if choice == 'y':
        interactive_demo()
    
    print("\n=== Summary ===")
    print("• Two Pointers is most efficient and truly in-place")
    print("• Python Slicing is most Pythonic but not in-place")
    print("• Recursive shows elegant recursive thinking")
    print("• Stack demonstrates LIFO property")
    print("• XOR Swap shows bit manipulation technique")
    print("• All solutions handle edge cases properly")