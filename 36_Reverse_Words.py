# Problem: Reverse the order of words in a sentence, ignoring extra spaces.
# Sample:  python   is fun → fun is python

sentence = input("Enter sentence : ").split()

reversed_sentence = reversed(sentence)  # Returns a reverse iterator 

print(" ".join(reversed_sentence))  # join() consumes iterable of strings
