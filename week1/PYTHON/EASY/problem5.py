# Valid Palindrome - THIS IS A CLASSIC INTERVIEW QUESTION. I WAS ASKED A VARIETY OF THIS.
# A palindrome is a word or sentence that is the exact same forward and backwards
#   (spaces not included for sentences)
# Given a string, see if you can make it a valid palindrome by deleting at most one letter
# If so, return True. If false, return False
#
# Note: A word may already be a palindrome, at which point you should return True
# Note: the word does not need to be an actual word.
# Note: A word will contain lowercase letters and no punctuation
#
# Example: civic -> civic (True)
# Example: race car -> race car (if you remove the space, it is a palindrome) True
# Example: radkar -> radar, rakar (True)
# Example: banana -> anana (True)
# Example: chick -> False

s1 = 'civic'
s2 = 'race car'
s3 = 'radkar'
s4 = 'banana'
s5 = 'chick'

def solution(s):
    # Your code goes here

print(solution(s1)) # True
print(solution(s2)) # True
print(solution(s3)) # True
print(solution(s4)) # True
print(solution(s5)) # False
