# First Unique Character
# Given a string, find the first non-repeating character in it and return both the index
#  and the character
# If it doesn't exist, return -1, and None.
# Note: all the input strings are lowercase

string1='alphabet'
string2='barbados'
string3='crunchy'
string4='baba'

def solution(string):
    # Your code goes here

print(solution(string1)) # 1, L (can be lowercase, just looks the same as 1)
print(solution(string2)) # 2, r
print(solution(string3)) # 1, r
print(solution(string4)) # -1, None
