# Problem: Count vowels, consonants and other characters in a sentence (case-insensitive).
# Sample: Hello World! → Vowels: 3, Consonants: 7, Others: 2

input_str = input("Enter : ").lower()

vowels = 0
consonants = 0
others = 0
for char in input_str:
    if char.isalpha():
        if char in "aeiou":
            vowels += 1

        else:
            consonants += 1

    else:
        others += 1

print(f"Vowels: {vowels}, Consonants: {consonants}, Others: {others}")
