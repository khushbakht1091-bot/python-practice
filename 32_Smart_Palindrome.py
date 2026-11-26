# Problem: Check if a sentence is a palindrome, ignoring case, spaces and punctuation.
# Sample: A man, a plan, a canal: Panama → Palindrome

orig_str = input("Enter sentence : ").lower()
cleaned_str = ""

# Cleaning the string
for char in orig_str:
    if char.isalnum():
        cleaned_str += char

# Comparing the cleaned string with its reverse
if cleaned_str == cleaned_str[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
