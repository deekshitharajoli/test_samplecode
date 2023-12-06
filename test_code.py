def is_palindrome(s):
    """Check if a string is a palindrome."""
    return s == s[::-1]

def reverse_string(s):
    """Reverse a string."""
    return s[::-1]

def count_vowels(s):
    """Count the number of vowels in a string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def remove_duplicates(s):
    """Remove duplicate characters from a string."""
    return ''.join(sorted(set(s), key=s.index))

def is_valid_email(email):
    """Validate an email address."""
    import re
    pattern = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(pattern, email)

def is_valid_password(password):
    """Validate a password."""
    # Add your password validation rules here
    # For example, check for minimum length, uppercase, lowercase, and special characters
    return len(password) >= 8 and any(c.isupper() for c in password) and any(c.islower() for c in password)

def main():
    # String manipulations
    input_string = "Hello, World!"
    print(f"Original String: {input_string}")
    print(f"Reversed String: {reverse_string(input_string)}")
    print(f"Palindrome Check: {is_palindrome(input_string)}")
    print(f"Count of Vowels: {count_vowels(input_string)}")
    print(f"Remove Duplicates: {remove_duplicates(input_string)}")

    # String validations
    email = "example@email.com"
    password = "StrongPassword123"

    print(f"\nEmail Validation: {is_valid_email(email)}")
    print(f"Password Validation: {is_valid_password(password)}")

if __name__ == "__main__":
    main()

