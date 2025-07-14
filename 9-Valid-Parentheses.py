"""
Problem: Valid Parentheses
Difficulty: Easy
Category: Basic Data Structures

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example:
Input: s = "()[]{}"
Output: true

Time Complexity Analysis:
- Solution 1 (Stack): O(n) time, O(n) space
- Solution 2 (Counter): O(n) time, O(1) space (for single type)
- Solution 3 (Recursive): O(n) time, O(n) space
"""

def is_valid_parentheses_stack(s):
    """
    Solution 1: Stack Approach (Most Efficient)
    Time Complexity: O(n) - We traverse the string once
    Space Complexity: O(n) - We use a stack to store opening brackets
    
    Algorithm:
    1. Use a stack to keep track of opening brackets
    2. For each closing bracket, check if it matches the top of stack
    3. If stack is empty when we encounter closing bracket, invalid
    4. If stack is not empty at end, invalid
    5. This is the most efficient approach for multiple bracket types
    """
    # Create a stack to store opening brackets
    stack = []
    
    # Define bracket pairs
    bracket_pairs = {')': '(', '}': '{', ']': '['}
    
    # Traverse each character in the string
    for char in s:
        # If it's an opening bracket, push to stack
        if char in '({[':
            stack.append(char)
        
        # If it's a closing bracket
        elif char in ')}]':
            # If stack is empty, no matching opening bracket
            if not stack:
                return False
            
            # Check if top of stack matches the closing bracket
            if stack.pop() != bracket_pairs[char]:
                return False
    
    # If stack is empty, all brackets are matched
    return len(stack) == 0


def is_valid_parentheses_counter(s):
    """
    Solution 2: Counter Approach (Only for single bracket type)
    Time Complexity: O(n) - We traverse the string once
    Space Complexity: O(1) - We only use counters
    
    Algorithm:
    1. Use counters for each type of bracket
    2. Increment for opening, decrement for closing
    3. If any counter goes negative, invalid
    4. If any counter is not zero at end, invalid
    5. This only works for single bracket type or simple cases
    """
    # Initialize counters for each bracket type
    round_count = 0  # ()
    curly_count = 0  # {}
    square_count = 0  # []
    
    # Traverse each character
    for char in s:
        if char == '(':
            round_count += 1
        elif char == ')':
            round_count -= 1
        elif char == '{':
            curly_count += 1
        elif char == '}':
            curly_count -= 1
        elif char == '[':
            square_count += 1
        elif char == ']':
            square_count -= 1
        
        # If any counter goes negative, invalid
        if round_count < 0 or curly_count < 0 or square_count < 0:
            return False
    
    # All counters must be zero for valid parentheses
    return round_count == 0 and curly_count == 0 and square_count == 0


def is_valid_parentheses_recursive(s):
    """
    Solution 3: Recursive Approach
    Time Complexity: O(n) - We process each character once
    Space Complexity: O(n) - Due to recursion call stack
    
    Algorithm:
    1. Use recursion to process brackets
    2. Base case: empty string is valid
    3. Recursive case: find matching pairs and recurse
    4. This demonstrates recursive thinking
    """
    def is_valid_helper(s, index=0):
        """Recursive helper function"""
        # Base case: reached end of string
        if index >= len(s):
            return True
        
        # If current character is closing bracket
        if s[index] in ')}]':
            return False
        
        # Find matching closing bracket
        opening = s[index]
        if opening == '(':
            closing = ')'
        elif opening == '{':
            closing = '}'
        elif opening == '[':
            closing = ']'
        else:
            return False
        
        # Find the matching closing bracket
        count = 1
        i = index + 1
        while i < len(s) and count > 0:
            if s[i] == opening:
                count += 1
            elif s[i] == closing:
                count -= 1
            i += 1
        
        # If no matching closing bracket found
        if count != 0:
            return False
        
        # Recursively check the substring between brackets
        if not is_valid_helper(s[index + 1:i - 1]):
            return False
        
        # Recursively check the remaining string
        return is_valid_helper(s, i)
    
    return is_valid_helper(s)


def is_valid_parentheses_simple(s):
    """
    Solution 4: Simple Stack with String Replacement
    Time Complexity: O(n²) - Due to string replacement
    Space Complexity: O(n) - We use a string
    
    Algorithm:
    1. Replace valid pairs with empty string
    2. Continue until no more replacements
    3. If final string is empty, valid
    4. This is simple but inefficient
    """
    # Keep replacing valid pairs until no more replacements
    while '()' in s or '{}' in s or '[]' in s:
        s = s.replace('()', '').replace('{}', '').replace('[]', '')
    
    # If string is empty, all brackets are matched
    return len(s) == 0


# Test cases to demonstrate all solutions
def test_valid_parentheses():
    """Test function to demonstrate all solutions"""
    
    test_cases = [
        "()",  # Simple valid
        "()[]{}",  # Multiple valid
        "(]",  # Invalid
        "([)]",  # Invalid
        "{[]}",  # Valid nested
        "(((",  # Invalid - too many opening
        ")))",  # Invalid - too many closing
        "",  # Empty string
        "({[]})",  # Complex valid
        "([{}])",  # Complex valid
        "([{])",  # Invalid
    ]
    
    print("=== Valid Parentheses Test Cases ===")
    for i, test_case in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        print(f"Input: '{test_case}'")
        
        # Test all solutions
        result1 = is_valid_parentheses_stack(test_case)
        result2 = is_valid_parentheses_counter(test_case)
        result3 = is_valid_parentheses_recursive(test_case)
        result4 = is_valid_parentheses_simple(test_case)
        
        print(f"Stack: {result1}")
        print(f"Counter: {result2}")
        print(f"Recursive: {result3}")
        print(f"Simple: {result4}")
        
        # Check if all solutions agree
        all_same = all([result1 == result2, result2 == result3, result3 == result4])
        print(f"All solutions agree: {all_same}")


# Main execution
if __name__ == "__main__":
    print("=== Valid Parentheses Problem - 4 Solutions ===")
    print("1. Stack (O(n) time, O(n) space) - RECOMMENDED")
    print("2. Counter (O(n) time, O(1) space) - Limited use")
    print("3. Recursive (O(n) time, O(n) space)")
    print("4. Simple String Replacement (O(n²) time, O(n) space)")
    print()
    
    # Run test cases
    test_valid_parentheses()
    
    print("\n=== Summary ===")
    print("• Stack is most efficient and handles all cases")
    print("• Counter is space-efficient but limited")
    print("• Recursive shows elegant recursive thinking")
    print("• Simple approach is intuitive but inefficient")
    print("• All solutions handle edge cases properly")