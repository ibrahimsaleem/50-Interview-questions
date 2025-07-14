"""
Problem: Valid Palindrome
Difficulty: Easy
Category: Arrays & Strings

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Time Complexity Analysis:
- Solution 1 (Two Pointers): O(n) time, O(1) space
- Solution 2 (String Reversal): O(n) time, O(n) space
- Solution 3 (Stack Approach): O(n) time, O(n) space
"""

import re  # For regular expressions

def is_palindrome_two_pointers(s):
    """
    Solution 1: Two Pointers Approach (Most Efficient)
    Time Complexity: O(n) - We traverse the string once
    Space Complexity: O(1) - We only use a constant amount of extra space
    
    Algorithm:
    1. Use two pointers: one at start, one at end
    2. Skip non-alphanumeric characters
    3. Compare characters (case-insensitive)
    4. Move pointers inward until they meet
    5. This is the most space-efficient approach
    """
    # Convert to lowercase and remove non-alphanumeric characters
    # re.sub() removes all characters that are not letters or digits
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
    
    # Initialize two pointers
    left = 0  # Start from beginning
    right = len(cleaned) - 1  # Start from end
    
    # Continue while pointers haven't met
    while left < right:
        # Compare characters from both ends
        if cleaned[left] != cleaned[right]:
            return False  # Not a palindrome
        
        # Move pointers inward
        left += 1
        right -= 1
    
    return True  # If we reach here, it's a palindrome


def is_palindrome_string_reversal(s):
    """
    Solution 2: String Reversal Approach
    Time Complexity: O(n) - We process the string once
    Space Complexity: O(n) - We create a new string
    
    Algorithm:
    1. Clean the string (remove non-alphanumeric, convert to lowercase)
    2. Create a reversed version of the cleaned string
    3. Compare original with reversed
    4. This is the most intuitive approach
    """
    # Convert to lowercase and remove non-alphanumeric characters
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
    
    # Compare with its reverse
    return cleaned == cleaned[::-1]  # [::-1] creates a reversed copy


def is_palindrome_stack_approach(s):
    """
    Solution 3: Stack Approach
    Time Complexity: O(n) - We process the string once
    Space Complexity: O(n) - We use a stack to store half the characters
    
    Algorithm:
    1. Clean the string (remove non-alphanumeric, convert to lowercase)
    2. Push first half of characters onto a stack
    3. For second half, pop from stack and compare
    4. This demonstrates a different way of thinking about the problem
    """
    # Convert to lowercase and remove non-alphanumeric characters
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
    
    # If string is empty or has one character, it's a palindrome
    if len(cleaned) <= 1:
        return True
    
    # Calculate the middle point
    mid = len(cleaned) // 2
    
    # Push first half onto stack
    stack = []
    for i in range(mid):
        stack.append(cleaned[i])
    
    # Start comparing from the middle (or middle + 1 if odd length)
    start = mid if len(cleaned) % 2 == 0 else mid + 1
    
    # Compare second half with popped elements from stack
    for i in range(start, len(cleaned)):
        if not stack or stack.pop() != cleaned[i]:
            return False
    
    return True


def is_palindrome_manual_cleaning(s):
    """
    Bonus Solution: Manual Character Filtering (No regex)
    Time Complexity: O(n) - We process the string once
    Space Complexity: O(n) - We create a new string
    
    This shows how to clean the string without using regular expressions
    """
    # Manual cleaning without regex
    cleaned = ""
    for char in s:
        # Check if character is alphanumeric
        if char.isalnum():
            cleaned += char.lower()
    
    # Compare with reverse
    return cleaned == cleaned[::-1]


# Test cases to demonstrate all solutions
def test_palindrome():
    """Test function to demonstrate all solutions"""
    
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("", True),
        ("a", True),
        ("ab", False),
        ("aba", True),
        ("Was it a car or a cat I saw?", True),
        ("hello", False),
        ("12321", True),
        ("No 'x' in Nixon", True)
    ]
    
    print("=== Valid Palindrome Test Cases ===")
    for i, (test_string, expected) in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        print(f"Input: '{test_string}'")
        print(f"Expected: {expected}")
        
        # Test all solutions
        result1 = is_palindrome_two_pointers(test_string)
        result2 = is_palindrome_string_reversal(test_string)
        result3 = is_palindrome_stack_approach(test_string)
        result4 = is_palindrome_manual_cleaning(test_string)
        
        print(f"Two Pointers: {result1}")
        print(f"String Reversal: {result2}")
        print(f"Stack Approach: {result3}")
        print(f"Manual Cleaning: {result4}")
        
        # Check if all solutions agree
        all_correct = all([result1 == expected, result2 == expected, 
                          result3 == expected, result4 == expected])
        print(f"All solutions correct: {all_correct}")


# Interactive demo
def interactive_demo():
    """Interactive demo where user can input their own test cases"""
    print("\n=== Valid Palindrome - Interactive Demo ===")
    print("Enter a string to check if it's a palindrome:")
    
    test_string = input("String: ").strip()
    
    print(f"\nResults for '{test_string}':")
    print(f"Two Pointers: {is_palindrome_two_pointers(test_string)}")
    print(f"String Reversal: {is_palindrome_string_reversal(test_string)}")
    print(f"Stack Approach: {is_palindrome_stack_approach(test_string)}")
    print(f"Manual Cleaning: {is_palindrome_manual_cleaning(test_string)}")


# Performance comparison
def performance_comparison():
    """Compare performance of different approaches"""
    import time
    
    # Create a long test string
    test_string = "A man, a plan, a canal: Panama" * 1000
    
    solutions = [
        ("Two Pointers", is_palindrome_two_pointers),
        ("String Reversal", is_palindrome_string_reversal),
        ("Stack Approach", is_palindrome_stack_approach),
        ("Manual Cleaning", is_palindrome_manual_cleaning)
    ]
    
    print("\n=== Performance Comparison ===")
    print(f"Testing with string of length {len(test_string)}")
    
    for name, func in solutions:
        start_time = time.time()
        result = func(test_string)
        end_time = time.time()
        
        print(f"{name}: {result} (Time: {(end_time - start_time)*1000:.2f} ms)")


# Main execution
if __name__ == "__main__":
    print("=== Valid Palindrome Problem - 4 Solutions ===")
    print("1. Two Pointers (O(n) time, O(1) space) - RECOMMENDED")
    print("2. String Reversal (O(n) time, O(n) space)")
    print("3. Stack Approach (O(n) time, O(n) space)")
    print("4. Manual Cleaning (O(n) time, O(n) space)")
    print()
    
    # Run test cases
    test_palindrome()
    
    # Performance comparison
    performance_comparison()
    
    # Ask if user wants interactive demo
    choice = input("\nWould you like to try your own test case? (y/n): ").lower()
    if choice == 'y':
        interactive_demo()
    
    print("\n=== Summary ===")
    print("• Two Pointers is most space-efficient")
    print("• String Reversal is most intuitive")
    print("• Stack Approach shows alternative thinking")
    print("• All solutions handle edge cases properly")
    print("• Remember to clean non-alphanumeric characters and ignore case")